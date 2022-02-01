from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.elements.payment_method import PaymentMethod
from edi_835_parser.elements.dollars import Dollars
from edi_835_parser.elements.integer import Integer
from edi_835_parser.elements.date import Date
from edi_835_parser.segments.utilities import split_segment, get_element


class FinancialInformation:
	identification = 'BPR'

	identifier = Identifier()
	amount_paid = Dollars()
	payment_method = PaymentMethod()
	routing_number = Integer()
	transaction_date = Date()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.transaction_handling_code = segment[1]
		self.amount_paid = segment[2]
		self.credit_debit_flag = segment[3]
		self.payment_method = segment[4]
		self.payment_format = segment[5]
		self.id_qualifier = get_element(segment, 6)
		self.id = get_element(segment, 7)
		self.acc_qualifier = get_element(segment, 8)
		self.sender_acc_no = get_element(segment, 9)
		self.routing_number = segment[13]
		self.transaction_date = segment[16]
		self.payer_id = get_element(segment, 10)
		self.account_no_qualifier = get_element(segment, 14)
		self.receiver_or_provider_acc_no = get_element(segment, 15)
		self.origin_company_code = get_element(segment, 11)

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
