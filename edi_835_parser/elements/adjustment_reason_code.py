from edi_835_parser.elements import Element, Code

# https://x12.org/codes/claim-adjustment-reason-codes
adjustment_reason_codes = {
	'45': 'Charge exceeds fee schedule maximum allowable or contracted/legislated fee arrangement.',
	'243': 'Services not authorized by network/primary care providers.',
	'29': 'The time limit for filing has expired.',
	'251': 'The attachment/other documentation that was received was incomplete or deficient.',
	'2': 'Coinsurnace Amount.',
	'96': 'Non-covered charge(s). See remark code.',
	'3': 'Co-payment Amount.',
	'16': 'Claim/service lacks information or has submission/billing error(s).',
	'B15':'This service/procedure requires that a qualifying service/procedure be received and covered. The qualifying other service/procedure has not been received/adjudicated.',
	'A1': 'Claim/Service denied. See remark code.',
	'1': 'Deductible Amount',
	'4': 'The procedure code is inconsistent with the modifier used. Usage: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.',
	'18': 'Exact duplicate claim/service (Use only with Group Code OA except where state workers\' compensation regulations requires CO)',
	'23': 'The impact of prior payer(s) adjudication including payments and/or adjustments. (Use only with Group Code OA)',
	'26': 'Expenses incurred prior to coverage.',
	'27': 'Expenses incurred after coverage terminated.',
	'97': 'The benefit for this service is included in the payment/allowance for another service/procedure that has already been adjudicated. Usage: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.',
	'109': 'Claim/service not covered by this payer/contractor. You must send the claim/service to the correct payer/contractor.',
	'151': 'Payment adjusted because the payer deems the information submitted does not support this many/frequency of services.',
	'234': 'This procedure is not paid separately. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)',
	'272': 'Coverage/program guidelines were not met.',
}


class AdjustmentReasonCode(Element):

	def parser(self, value: str) -> Code:
		description = adjustment_reason_codes.get(value, None)
		return Code(value, description)
