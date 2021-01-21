from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.elements.dollars import Dollars
from edi_835_parser.elements.service_code import ServiceCode
from edi_835_parser.elements.integer import Integer
from edi_835_parser.segments.utilities import split_segment


class Service:
	identification = 'SVC'

	identifier = Identifier()
	charge_amount = Dollars()
	paid_amount = Dollars()
	service_code = ServiceCode()
	units = Integer()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.service_code = segment[1]
		self.charge_amount = segment[2]
		self.paid_amount = segment[3]
		self.units = segment[5]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
