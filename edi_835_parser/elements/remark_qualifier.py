from edi_835_parser.elements import Element

remark_qualifiers = {
	'HE': 'claim payment'
}


class RemarkQualifier(Element):

	def parser(self, value: str) -> str:
		return remark_qualifiers.get(value, value)
