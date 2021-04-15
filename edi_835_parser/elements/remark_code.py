from edi_835_parser.elements import Element, Code

# https://x12.org/codes/remittance-advice-remark-codes
remark_codes = {
	'N630': 'Referral not authorized by attending physician.',
	'N650': 'This policy was not in effect for this date of loss. No coverage is available.',
	'M53': 'Missing/incomplete/invalid days or units of service.',
	'M15': 'Separately billed services/tests have been bundled as they are considered components of the same procedure. Separate payment is not allowed.',
	'M80': 'Not covered when performed during the same session/date as a previously processed service for the patient.',
	'M86': 'Service denied because payment already made for same/similar procedure within set time frame.',
	'MA130': 'Your claim contains incomplete and/or invalid information, and no appeal rights are afforded because the claim is unprocessable. Please submit a new claim with the complete/correct information.',
	'N122': 'Add-on code cannot be billed by itself.',
	'N20': 'Service not payable with other service rendered on the same date.',
	'N6': 'Under FEHB law (U.S.C. 8904(b)), we cannot pay more for covered care than the amount Medicare would have allowed if the patient were enrolled in Medicare Part A and/or Medicare Part B.',
	'N640': 'Exceeds number/frequency approved/allowed within time period.',
	'N674': 'Not covered unless a pre-requisite procedure/service has been provided.',
	'N702': 'Decision based on review of previously adjudicated claims or for claims in process for the same/similar type of services.',
	'N781': 'Alert: Patient is a Medicaid/ Qualified Medicare Beneficiary. Review your records for any wrongfully collected deductible. This amount may be billed to a subsequent payer.',
	'N782': 'Alert: Patient is a Medicaid/ Qualified Medicare Beneficiary. Review your records for any wrongfully collected coinsurance. This amount may be billed to a subsequent payer.',
	'N807': 'Payment adjustment based on the Merit-based Incentive Payment System (MIPS).',
}


class RemarkCode(Element):

	def parser(self, value: str) -> Code:
		description = remark_codes.get(value, None)
		return Code(value, description)
