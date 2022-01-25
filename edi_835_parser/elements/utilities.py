from typing import List


def split_element(segment: str) -> List[str]:
	"""different payers use different characters to delineate sub-elements"""
	arrow = '^'
	colon = ':'
	greater_than = '>'

	arrow_segment_count = len(segment.split(arrow))
	colon_segment_count = len(segment.split(colon))
	greater_than_segment_count = len(segment.split(greater_than))

	if arrow_segment_count > colon_segment_count:
		return segment.split(arrow)
	elif greater_than_segment_count > colon_segment_count:
		return segment.split(greater_than)
	else:
		return segment.split(colon)