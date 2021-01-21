from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.elements.payment_method import PaymentMethod
from edi_835_parser.elements.dollars import Dollars
from edi_835_parser.elements.integer import Integer
from edi_835_parser.segments.utilities import split_segment


class FinancialInformation:
	identification = 'BPR'

	identifier = Identifier()
	amount_paid = Dollars()
	payment_method = PaymentMethod()
	routing_number = Integer()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.amount_paid = segment[2]
		self.payment_method = segment[4]
		self.routing_number = segment[13]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
