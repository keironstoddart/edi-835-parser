from edi_835_parser.elements import Element

payment_methods = {
	'ACH': 'automatic deposit',
	'CHK': 'check',
	'NON': 'no payment'
}


class PaymentMethod(Element):

	def parser(self, value: str) -> str:
		value = value.strip()
		return payment_methods.get(value, value)
