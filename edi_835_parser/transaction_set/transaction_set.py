from typing import List, Iterator, Optional
from collections import namedtuple

import pandas as pd

from edi_835_parser.loops.claim import Claim as ClaimLoop
from edi_835_parser.loops.transaction import Transaction as TransactionLoop
from edi_835_parser.loops.service import Service as ServiceLoop
from edi_835_parser.loops.organization import Organization as OrganizationLoop
from edi_835_parser.segments.utilities import find_identifier
from edi_835_parser.segments.interchange import Interchange as InterchangeSegment

BuildAttributeResponse = namedtuple('BuildAttributeResponse', 'key value segment segments')


class TransactionSet:

	def __init__(
			self,
			interchange: InterchangeSegment,
			transactions: List[TransactionLoop]
	):
		self.interchange = interchange
		self.transactions = transactions

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())

	def to_dataframe(self) -> tuple[pd.DataFrame]:
		"""flatten the remittance advice by service to a pandas DataFrame"""
		remits_df = []
		remit_payers_df = []

		for transaction in self.transactions:
			for claim in transaction.claims:
				for service in claim.services:

					remits_dict, remit_payers_dict = TransactionSet.serialize_service(
						claim,
						service,
						transaction
					)

				remits_df.append(remits_dict)
				remit_payers_df.append(remit_payers_dict)

		remits_df = pd.DataFrame(remits_df)
		remit_payers_df = pd.DataFrame(remit_payers_df)

		return remits_df, remit_payers_df

	@staticmethod
	def serialize_service(
			claim: ClaimLoop,
			service: ServiceLoop,
			transaction: TransactionLoop
	) -> tuple:
		# # if the service doesn't have a start date assume the service and claim dates match
		# start_date = None
		# if service.service_period_start:
		# 	start_date = service.service_period_start.date
		# elif claim.claim_statement_period_start:
		# 	start_date = claim.claim_statement_period_start.date
		#
		# # if the service doesn't have an end date assume the service and claim dates match
		# end_date = None
		# if service.service_period_end:
		# 	end_date = service.service_period_end.date
		# elif claim.claim_statement_period_end:
		# 	end_date = claim.claim_statement_period_end.date

		remits_dict = {
			'edi_transacrion_id_st02': transaction.transaction.transaction_set_control_no,
			'patient_control_id': claim.claim.patient_control_number,
			'patient_id_qualifier': claim.patient.identification_code_qualifier,
			'patient_id': claim.patient.identification_code,
			'patient_last_name': claim.patient.last_name,
			'patient_first_name': claim.patient.first_name,
			'patient_middle_name': claim.patient.middle_name,
			'patient_name_suffix': claim.patient.name_suffix,
			'patient_name_prefix': claim.patient.name_prefix,
			'payer_id': transaction.payer.identification_code,
			'payer_name': transaction.payer.name,
			'bt_facility_type_code_clp08': claim.claim.facility_type_code,
			'bt_facility_type_code_clp09': claim.claim.claim_frequency_code,
			'payee_id_qualifier': transaction.payee.identification_code_qualifier,
			'payee_id': transaction.payee.identification_code,
			'provider_entity_type_qualifier': claim.rendering_provider.type,
			'provider_id_qualifier': claim.rendering_provider.identification_code_qualifier,
			'provider_id': claim.rendering_provider.identification_code,
			'provider_name': claim.rendering_provider.name if claim.rendering_provider else None,
			'provider_first_name': claim.rendering_provider.first_name,
			'provider_middle_name': claim.rendering_provider.middle_name,
			'provider_suffix': claim.rendering_provider.name_suffix,
			'provider_prefix': claim.rendering_provider.name_prefix,
			'claim_received_date': claim.claim_received_date.date,
			'claim_paid_date': transaction.financial_information.transaction_date,
			'claim_status': claim.claim.status,
			'claim_total_charge_amount': claim.claim.charge_amount,
			'claim_payment_amount': claim.claim.paid_amount,
			'claim_patient_responsibility': claim.claim.patient_responsibility_amount,
			'claim_filing_indicator': claim.claim.claim_filing_indicator_code,
			'payer_claim_control_number': claim.claim.payer_claim_control_number,
			'drg_code': claim.claim.drg_code,
			'corrected_insured_last_name': claim.insured.last_name if claim.insured else None,
			'corrected_insured_first_name': claim.insured.first_name if claim.insured else None,
			'corrected_insured_middle_name': claim.insured.middle_name if claim.insured else None,
			'corrected_insured_prefix': claim.insured.name_prefix if claim.insured else None,
			'corrected_insured_suffix': claim.insured.name_suffix if claim.insured else None,
			'corrected_insured_id_qualifier': claim.insured.identification_code_qualifier if claim.insured else None,
			'corrected_insured_id': claim.insured.identification_code if claim.insured else None,
			'claim_statement_period_start': claim.claim_statement_period_start.date if claim.claim_statement_period_start else None,
			'claim_statement_period_end': claim.claim_statement_period_end.date if claim.claim_statement_period_end else None,
			'claim_coverage_expiration': claim.claim_coverage_expiration.date if claim.claim_coverage_expiration else None,
			'claim_coverage_amount': claim.amount.amount,
			'claim_contract_code': claim.claim_contract_code.value if claim.claim_contract_code else None,

		}

		remit_payers_dict = {
			'edi_transacrion_id_st02': transaction.transaction.transaction_set_control_no,
			'payer_id': transaction.payer.identification_code,
			'payer_name': transaction.payer.name,
			'payer_address_line1': transaction.payer_address.address_line1,
			'payer_address_line2': transaction.payer_address.address_line2,
			'payer_city': transaction.payer_location.city,
			'payer_state': transaction.payer_location.state,
			'payer_zip': transaction.payer_location.zip_code,
			'payer_country': transaction.payer_location.country,
			'payer_contact_business': transaction.payer_contact_business.communication_no_or_url,
			'payer_contact_business_qualifier': transaction.payer_contact_business.communication_no_or_url_qualifier,
			'payer_contact_business_name': transaction.payer_contact_business.name,
			'payer_contact_web': transaction.payer_contact_web.communication_no_or_url if transaction.payer_contact_web else None,
			'payer_contact_web_qualifier': transaction.payer_contact_web.communication_no_or_url_qualifier if transaction.payer_contact_web else None,
			'payer_contact_web_name': transaction.payer_contact_web.name if transaction.payer_contact_web else None


		}

		remit_payment_info_dict = {
			'edi_transacrion_id_st02': transaction.transaction.transaction_set_control_no,

		}

		return remits_dict, remit_payers_dict

	@classmethod
	def build(cls, file_path: str) -> 'TransactionSet':
		interchange = None
		transactions = []

		with open(file_path) as f:
			file = f.read()

		segments = file.split('~')
		segments = [segment.strip() for segment in segments]

		segments = iter(segments)
		segment = None

		while True:
			response = cls.build_attribute(segment, segments)
			segment = response.segment
			segments = response.segments

			# no more segments to parse
			if response.segments is None:
				break

			if response.key == 'interchange':
				interchange = response.value


			if response.key == 'transaction':
				transactions.append(response.value)


			# if response.key in cls.terminating_identifiers:

		return TransactionSet(interchange, transactions)

	@classmethod
	def build_attribute(cls, segment: Optional[str], segments: Iterator[str]) -> BuildAttributeResponse:
		if segment is None:
			try:
				segment = segments.__next__()
			except StopIteration:
				return BuildAttributeResponse(None, None, None, None)

		identifier = find_identifier(segment)

		if identifier == InterchangeSegment.identification:
			interchange = InterchangeSegment(segment)
			return BuildAttributeResponse('interchange', interchange, None, segments)


		if identifier == OrganizationLoop.initiating_identifier:
			organization, segments, segment = OrganizationLoop.build(segment, segments)
			return BuildAttributeResponse('organization', organization, segment, segments)

		elif identifier == ClaimLoop.initiating_identifier:
			claim, segments, segment = ClaimLoop.build(segment, segments)
			return BuildAttributeResponse('claim', claim, segment, segments)

		elif identifier == TransactionLoop.initiating_identifier:
			transaction, segments, segment = TransactionLoop.build(segment, segments)
			return BuildAttributeResponse('transaction', transaction, segment, segments)


		else:
			return BuildAttributeResponse(None, None, None, segments)


if __name__ == '__main__':
	pass