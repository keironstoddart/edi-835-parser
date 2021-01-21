from edi_835_parser.elements import Element

# https://ushik.ahrq.gov/dr.ui.drValueDomain_View?system=mdr&ValueDomainID=4933000&CallingRoutine=$CallingRoutine$&OrganizationID=3&RecordOffset=11&Referer=ValueDomain
identification_code_qualifiers = {
	'MI': 'member identification number',
	'C': "insured's changed unique identification number",
	'PC': 'provider commercial number',
	'XX': 'national provider id',

}


class IdentificationCodeQualifier(Element):

	def parser(self, value: str) -> str:
		return identification_code_qualifiers.get(value, value)
