from edi_835_parser.elements import Element, Code

# https://ushik.ahrq.gov/ViewItemDetails?&system=sdo&itemKey=133213000
reference_qualifiers = {
	'6R': 'provider control number',
	'0K': 'policy form identifying number',
	'PQ': 'payee identification',
	'TJ': 'federal taxpayer identification number',
	'LU': 'location number'
}


class ReferenceQualifier(Element):

	def parser(self, value: str) -> Code:
		description = reference_qualifiers.get(value, None)
		return Code(value, description)
