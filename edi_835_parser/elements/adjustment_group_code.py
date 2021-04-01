from edi_835_parser.elements import Element

# https://x12.org/codes/claim-adjustment-group-codes
group_codes = {
	'CR': 'corrections and reversals',
	'OA': 'other adjustment',
	'PR': 'patient responsibility',
	'CO': 'contractual obligation',
	'PI': 'payor initiated reduction',
}


class AdjustmentGroupCode(Element):

	def parser(self, value: str) -> str:
		return group_codes.get(value, value)
