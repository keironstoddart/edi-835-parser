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

		return data

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