from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.elements.dollars import Dollars
from edi_835_parser.elements.adjustment_group_code import AdjustmentGroupCode
from edi_835_parser.elements.adjustment_reason_code import AdjustmentReasonCode
from edi_835_parser.segments.utilities import split_segment


class ServiceAdjustment:
	identification = 'CAS'

	identifier = Identifier()
	group_code = AdjustmentGroupCode()
	reason_code = AdjustmentReasonCode()
	amount = Dollars()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.group_code = segment[1]
		self.reason_code = segment[2]
		self.amount = segment[3]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
