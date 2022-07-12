from edi_835_parser.elements.utilities import split_element, _identify_delim


def test_delim_identification():
    element = 'HC^99454'
    delim = _identify_delim(element)
    assert delim == '^'

    element = 'HC:99454'
    delim = _identify_delim(element)
    assert delim == ':'

    element = 'HC:99454:23'
    delim = _identify_delim(element)
    assert delim == ':'


def test_split_element():
    element = 'HC^99454'
    sub_elements = split_element(element)

    assert len(sub_elements) == 2

    element = 'HC:99454:23'
    sub_elements = split_element(element)

    assert len(sub_elements) == 3
