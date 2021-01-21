from typing import List

def split_element(segment: str) -> List[str]:
	"""different payers use different characters to delineate sub-elements"""
	arrow = '^'
	colon = ':'

	arrow_segment_count = len(segment.split(arrow))
	colon_segment_count = len(segment.split(colon))

	if arrow_segment_count > colon_segment_count:
		return segment.split(arrow)
	else:
		return segment.split(colon)