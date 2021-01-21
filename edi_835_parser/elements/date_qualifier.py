from edi_835_parser.elements import Element

# https://ediacademy.com/blog/x12-date-time-qualifiers/
date_qualifiers = {
	'050': 'received',
	'150': 'service period start',
	'151': 'service period end',
	'472': 'service'
}


class DateQualifier(Element):

	def parser(self, value: str) -> str:
		return date_qualifiers.get(value, value)
