from typing import Optional

from edi_835_parser.elements import Element
from edi_835_parser.elements.utilities import split_element


class ServiceModifier(Element):

	def parser(self, value: str) -> Optional[str]:
		value = split_element(value)
		if len(value) > 2:
			return value[2]
