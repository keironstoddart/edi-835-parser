from typing import List, Iterable

import pandas as pd

from edi_835_parser.transaction_set.transaction_set import TransactionSet


class TransactionSets:

	def __init__(self, transaction_sets: List[TransactionSet]):
		self.transaction_sets = transaction_sets

	def __iter__(self) -> Iterable[TransactionSet]:
		yield from self.transaction_sets

	def __len__(self) -> int:
		return len(self.transaction_sets)

	def __repr__(self):
		return '\n'.join(str(transaction_set) for transaction_set in self)

	def to_dataframe(self) -> pd.DataFrame:
		data = pd.DataFrame()
		for transaction_set in self:
			data = pd.concat([data, transaction_set.to_dataframe()])

		data = TransactionSets.sort_columns(data)
		return data

	@staticmethod
	def sort_columns(data: pd.DataFrame) -> pd.DataFrame:
		substrings = ['adj', 'ref', 'rem']
		variable_columns = [c for c in data.columns if any(sub_string in c for sub_string in substrings)]
		variable_columns = sorted(variable_columns)

		static_columns = [c for c in data.columns if c not in variable_columns]

		data = data[static_columns + variable_columns]
		return data

	def sum_payments(self) -> float:
		amount = 0
		for transaction_set in self:
			amount += transaction_set.financial_information.amount_paid

		return amount

	def count_claims(self) -> int:
		count = 0
		for transaction_set in self:
			count += len(transaction_set.claims)

		return count

	def count_patients(self) -> int:
		patients = []
		for transaction_set in self:
			for claim in transaction_set.claims:
				patient = claim.patient
				patients.append(patient.identification_code)

		patients = set(patients)
		return len(patients)