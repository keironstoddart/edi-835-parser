from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.elements.dollars import Dollars
from edi_835_parser.elements.amount_qualifier import AmountQualifier
from edi_835_parser.segments.utilities import split_segment


class Amount:
	identification = 'AMT'

	identifier = Identifier()
	qualifier = AmountQualifier()
	paid_amount = Dollars()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.qualifier = segment[1]
		self.paid_amount = segment[2]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
