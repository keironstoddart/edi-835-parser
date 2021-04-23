from edi_835_parser.elements import Element, Code

remark_qualifiers = {
	'HE': 'claim payment'
}


class RemarkQualifier(Element):

	def parser(self, value: str) -> Code:
		description = remark_qualifiers.get(value, None)
		return Code(value, description)
