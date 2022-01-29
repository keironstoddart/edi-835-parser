import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import edi_835_parser

current_path = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def blue_cross_nc_sample():
	path = current_path + '/test_edi_835_files/blue_cross_nc_sample.txt'
	return edi_835_parser.parse(path)


@pytest.fixture
def emedny_sample():
	path = current_path + '/test_edi_835_files/emedny_sample.txt'
	return edi_835_parser.parse(path)

# @pytest.fixture
# def quadax_sample_835():
# 	path = current_path + '/test_edi_835_files/sample_835.txt'
# 	return edi_835_parser.parse(path)



@pytest.fixture
def all_samples():
	path = current_path + '/test_edi_835_files'
	return edi_835_parser.parse(path)
