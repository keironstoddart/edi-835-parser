from typing import List
from collections import defaultdict


def split_element(segment: str) -> List[str]:
    """different payers use different characters to delineate sub-elements"""
    delim = _identify_delim(segment)
    return segment.split(delim)


def _identify_delim(segment: str) -> str:
    delim_candidates = ['^', ':', '>', '<']
    
    value_counts = defaultdict(int)
    for delim in delim_candidates:
        value_counts[delim] = segment.count(delim)
    
    delim = max(value_counts, key=value_counts.get)

    return delim
