from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.elements.remark_qualifier import RemarkQualifier
from edi_835_parser.elements.remark_code import RemarkCode
from edi_835_parser.segments.utilities import split_segment


class Remark:
	identification = 'LQ'

	identifier = Identifier()
	qualifer = RemarkQualifier()
	code = RemarkCode()

	def __init__(self, segment: str):
		self.segment = segment
		segment = split_segment(segment)

		self.identifier = segment[0]
		self.qualifier = segment[1]
		self.code = segment[2]

	def __repr__(self):
		return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
	pass
