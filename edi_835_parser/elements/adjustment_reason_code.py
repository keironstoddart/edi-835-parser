from edi_835_parser.elements import Element

# https://x12.org/codes/claim-adjustment-reason-codes
reason_codes = {
	'45': 'Charge exceeds fee schedule maximum allowable or contracted/legislated fee arrangement.',
	'243': 'Services not authorized by network/primary care providers.',
	'29': 'The time limit for filing has expired.',
	'251': 'The attachment/other documentation that was received was incomplete or deficient.',
}


class AdjustmentReasonCode(Element):

	def parser(self, value: str) -> str:
		return reason_codes.get(value, value)
