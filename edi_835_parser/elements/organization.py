from edi_835_parser.elements import Element

organizations = {
	'AV09311993': 'Availity',
	'ZIRMED': 'Zirmed'
}


class Organization(Element):

	def parser(self, value: str) -> str:
		value = value.strip()
		return organizations.get(value, value)
