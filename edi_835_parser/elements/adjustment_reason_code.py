from edi_835_parser.elements import Element

# https://x12.org/codes/claim-adjustment-reason-codes
reason_codes = {
	'45': 'Charge exceeds fee schedule maximum allowable or contracted/legislated fee arrangement.',
	'243': 'Services not authorized by network/primary care providers.',
	'29': 'The time limit for filing has expired.',
	'251': 'The attachment/other documentation that was received was incomplete or deficient.',
	'2': 'Coinsurnace Amount.',
	'96': 'Non-covered charge(s). See remark code.',
	'3': 'Co-payment Amount.',
	'16': 'Claim/service lacks information or has submission/billing error(s).',
	'B15':'This service/procedure requires that a qualifying service/procedure be received and covered. The qualifying other service/procedure has not been received/adjudicated.',
	'A1':'Claim/Service denied. See remark code.',

}


class AdjustmentReasonCode(Element):

	def parser(self, value: str) -> str:
		return reason_codes.get(value, value)
