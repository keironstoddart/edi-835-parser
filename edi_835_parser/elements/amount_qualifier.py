from edi_835_parser.elements import Element

# https://ushik.ahrq.gov/ViewItemDetails?system=mdr&itemKey=133081000
amount_qualifiers = {
	'B6': 'allowed - actual',
}


class AmountQualifier(Element):

	def parser(self, value: str) -> str:
		return amount_qualifiers.get(value, value)
