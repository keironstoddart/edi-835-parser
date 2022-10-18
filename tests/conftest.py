import os
import pytest
import edi_835_parser


@pytest.fixture
def base_test_directory():
	return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def test_input_directory(base_test_directory):
	return base_test_directory + '/test_edi_835_files'


@pytest.fixture
def test_output_directory(base_test_directory):
	return base_test_directory + '/output'


@pytest.fixture
def blue_cross_nc_sample(test_input_directory):
	path = test_input_directory + '/blue_cross_nc_sample.txt'
	return edi_835_parser.parse(path)


@pytest.fixture
def emedny_sample(test_input_directory):
	path = test_input_directory + '/emedny_sample.txt'
	return edi_835_parser.parse(path)


@pytest.fixture
def united_healthcare_legacy_sample(test_input_directory):
	path = test_input_directory + '/united_healthcare_legacy_sample.txt'
	return edi_835_parser.parse(path)


@pytest.fixture
def all_samples(test_input_directory):
	return edi_835_parser.parse(test_input_directory)
