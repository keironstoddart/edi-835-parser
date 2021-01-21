from typing import Tuple, Iterator, Optional, List
from warnings import warn

from edi_835_parser.segments.service import Service as ServiceSegment
from edi_835_parser.segments.claim import Claim as ClaimSegment
from edi_835_parser.segments.date import Date as DateSegment
from edi_835_parser.segments.reference import Reference as ReferenceSegment
from edi_835_parser.segments.amount import Amount as AmountSegment
from edi_835_parser.segments.service_adjustment import ServiceAdjustment as ServiceAdjustmentSegment
from edi_835_parser.segments.remark import Remark as RemarkSegment
from edi_835_parser.segments.utilities import find_identifier


class Service:
	initiating_identifier = ServiceSegment.identification
	terminating_identifiers = [
		ServiceSegment.identification,
		ClaimSegment.identification,
		'SE'
	]

	def __init__(
			self,
			service: ServiceSegment = None,
			dates: List[DateSegment] = None,
			references: List[ReferenceSegment] = None,
			remark: RemarkSegment = None,
			amount: AmountSegment = None,
			adjustment: ServiceAdjustmentSegment = None
	):
		self.service = service
		self.dates = dates if dates else []
		self.references = references if references else []
		self.remark = remark
		self.amount = amount
		self.adjustment = adjustment

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())

	@property
	def service_date(self) -> Optional[DateSegment]:
		service_date = [d for d in self.dates if d.qualifier == 'service']
		assert len(service_date) <= 1, f'{self.dates}'

		if len(service_date) == 1:
			return service_date[0]

	@property
	def service_period_start(self) -> Optional[DateSegment]:
		service_period_start = [d for d in self.dates if d.qualifier == 'service period start']
		assert len(service_period_start) <= 1, f'{self.dates}'

		if len(service_period_start) == 1:
			return service_period_start[0]
		else:
			return self.service_date

	@property
	def service_period_end(self) -> Optional[DateSegment]:
		service_period_end = [d for d in self.dates if d.qualifier == 'service period end']
		assert len(service_period_end) <= 1

		if len(service_period_end) == 1:
			return service_period_end[0]
		else:
			return self.service_date

	@classmethod
	def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Service', Optional[str], Optional[Iterator[str]]]:
		service = Service()
		service.service = ServiceSegment(segment)

		while True:
			try:
				segment = segments.__next__()
				identifier = find_identifier(segment)

				if identifier == DateSegment.identification:
					date = DateSegment(segment)
					service.dates.append(date)

				elif identifier == AmountSegment.identification:
					service.amount = AmountSegment(segment)

				elif identifier == RemarkSegment.identification:
					service.remark = RemarkSegment(segment)

				elif identifier == ReferenceSegment.identification:
					reference = ReferenceSegment(segment)
					service.references.append(reference)

				elif identifier == ServiceAdjustmentSegment.identification:
					service.adjustment = ServiceAdjustmentSegment(segment)

				elif identifier in cls.terminating_identifiers:
					return service, segment, segments

				else:
					message = f'Identifier: {identifier} not handled in service loop.'
					warn(message)

			except StopIteration:
				return service, None, None


if __name__ == '__main__':
	pass
