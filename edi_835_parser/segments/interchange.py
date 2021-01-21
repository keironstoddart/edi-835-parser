from edi_835_parser.elements.authorization_information_qualifier import AuthorizationInformationQualifier
from edi_835_parser.elements.organization import Organization
from edi_835_parser.elements.date import Date
from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.segments.utilities import split_segment


class Interchange:
	identification = 'ISA'

	identifier = Identifier()
	authorization_information_qualifier = AuthorizationInformationQualifier()
	sender = Organization()
	receiver = Organization()
	transmission_date = Date()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.authorization_information_qualifier = segment[1]
		self.sender = segment[6]
		self.receiver = segment[8]
		self.transmission_date = segment[9] + segment[10]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
