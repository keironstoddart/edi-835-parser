from edi_835_parser.elements import Element

# https://magnacare.com/wp-content/uploads/pdf/MagnacareCompanionGuide_835_5010A1.pdf
entity_types = {
	'1': 'person',
	'2': 'entity',
}


class EntityType(Element):

	def parser(self, value: str) -> str:
		return entity_types.get(value, value)
