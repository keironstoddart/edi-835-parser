from edi_835_parser.elements import Element

# https://magnacare.com/wp-content/uploads/pdf/MagnacareCompanionGuide_835_5010A1.pdf
entity_types = {
	'1': 'person',
	'2': 'not person',  # changed the value of '2' from 'entity' to 'not person'
}


class EntityType(Element):

	def parser(self, value: str) -> str:
		return entity_types.get(value, value)
