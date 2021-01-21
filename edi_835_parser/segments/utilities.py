from typing import List, Optional


def split_segment(segment: str) -> List[str]:
	"""different payers use different characters to delineate elements"""
	asterisk = '*'
	pipe = '|'

	asterisk_segment_count = len(segment.split(asterisk))
	pipe_segment_count = len(segment.split(pipe))

	if asterisk_segment_count > pipe_segment_count:
		return segment.split(asterisk)
	else:
		return segment.split(pipe)


def find_identifier(segment) -> str:
	segment = split_segment(segment)
	return segment[0]

def get_element(segment: List[str], index: int) -> Optional[str]:
	element = None
	if index < len(segment):
		element =  segment[index]

	return element
