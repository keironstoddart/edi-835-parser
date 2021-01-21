from typing import List, Iterator, Optional
from collections import namedtuple

import pandas as pd

from edi_835_parser.loops.claim import Claim as ClaimLoop
from edi_835_parser.loops.organization import Organization as OrganizationLoop
from edi_835_parser.segments.utilities import find_identifier
from edi_835_parser.segments.interchange import Interchange as InterchangeSegment
from edi_835_parser.segments.financial_information import FinancialInformation as FinancialInformationSegment

BuildAttributeResponse = namedtuple('BuildAttributeResponse', 'key value segment segments')


class TransactionSet:

	def __init__(
			self,
			interchange: InterchangeSegment,
			financial_information: FinancialInformationSegment,
			claims: List[ClaimLoop],
			organizations: List[OrganizationLoop]
	):
		self.interchange = interchange
		self.financial_information = financial_information
		self.claims = claims
		self.organizations = organizations

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())

	@property
	def payer(self) -> OrganizationLoop:
		payer = [o for o in self.organizations if o.organization.type == 'payer']
		assert len(payer) == 1
		return payer[0]

	def to_dataframe(self) -> pd.DataFrame:
		"""flatten the remittance advice by service to a pandas DataFrame"""
		services = []
		for claim in self.claims:
			for service in claim.services:
				services.append({
					'claim_index': claim.claim.index,
					'patient': claim.patient.name,
					'code': service.service.service_code,
					'units': service.service.units,
					'paid_amount': service.service.paid_amount,
					'charge_amount': service.service.charge_amount,
					'payer': self.payer.organization.name,
					'service_period_start': service.service_period_start.date,
					'service_period_end': service.service_period_end.date,
					'note': service.adjustment.reason_code if service.adjustment else None,
					'rendering_provider': claim.rendering_provider.name if claim.rendering_provider else None,
				})
		return pd.DataFrame(services)

	@classmethod
	def build(cls, file_path: str) -> 'TransactionSet':
		interchange = None
		financial_information = None
		claims = []
		organizations = []

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

			if response.key == 'financial information':
				financial_information = response.value

			if response.key == 'organization':
				organizations.append(response.value)

			if response.key == 'claim':
				claims.append(response.value)

		return TransactionSet(interchange, financial_information, claims, organizations)

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

		if identifier == FinancialInformationSegment.identification:
			financial_information = FinancialInformationSegment(segment)
			return BuildAttributeResponse('financial information', financial_information, None, segments)

		if identifier == OrganizationLoop.initiating_identifier:
			organization, segments, segment = OrganizationLoop.build(segment, segments)
			return BuildAttributeResponse('organization', organization, segment, segments)

		elif identifier == ClaimLoop.initiating_identifier:
			claim, segments, segment = ClaimLoop.build(segment, segments)
			return BuildAttributeResponse('claim', claim, segment, segments)

		else:
			return BuildAttributeResponse(None, None, None, segments)


if __name__ == '__main__':
	pass