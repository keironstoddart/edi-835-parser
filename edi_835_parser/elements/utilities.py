from typing import List

def split_element(segment: str) -> List[str]:
    """different payers use different characters to delineate sub-elements"""
    delim_dict = {x:0 for x in ['^',':',">"]}

    for delim in delim_dict:
        delim_dict[delim] = segment.count(delim)

    return segment.split(max(delim_dict, key=delim_dict.get))
