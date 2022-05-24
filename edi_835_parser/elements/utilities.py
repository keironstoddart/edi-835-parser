from typing import List
import re
def split_element(segment: str) -> List[str]:
	"""different payers use different characters to delineate sub-elements"""
	return re.split(r"\^|:|>", segment)