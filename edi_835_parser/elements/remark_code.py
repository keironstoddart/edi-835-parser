from edi_835_parser.elements import Element

# https://x12.org/codes/remittance-advice-remark-codes
remark_codes = {
	'N630': 'Referral not authorized by attending physician.'
}


class RemarkCode(Element):

	def parser(self, value: str) -> str:
		return remark_codes.get(value, value)
