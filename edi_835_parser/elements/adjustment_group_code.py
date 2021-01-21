from edi_835_parser.elements import Element

group_codes = {
	'CR': 'corrections and reversals',
	'OA': 'other adjustment',
	'PR': 'patient responsibility'
}


class AdjustmentGroupCode(Element):

	def parser(self, value: str) -> str:
		return group_codes.get(value, value)
