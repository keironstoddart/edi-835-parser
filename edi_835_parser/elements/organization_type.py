from edi_835_parser.elements import Element

organization_types = {
	'PE': 'payee',
	'PR': 'payer',
}


class OrganizationType(Element):

	def parser(self, value: str) -> str:
		value = value.strip()
		return organization_types.get(value, value)
