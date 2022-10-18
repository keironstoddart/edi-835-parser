import pandas.testing

from edi_835_parser.cli.main import main
import pytest
import pathlib
from pandas import DataFrame, read_csv


def test_cli_validation(tmp_path: pathlib.Path, base_test_directory):
    """
    Tests CLI Validations, verifying appropriate exceptions are raised.

    :param tmp_path: pytest fixture which provides a temporary directory for the test case
    :param test_directory: conftest fixture which provides the path to test edi files

    """
    args = ['/invalid/directory', tmp_path.as_posix() + '/835.csv']
    with pytest.raises(FileNotFoundError, match='input location'):
        main(args)

    args = [base_test_directory, '/invalid/directory/835.csv']
    with pytest.raises(FileNotFoundError, match='csv output'):
        main(args)


@pytest.mark.parametrize("edi_file_name, csv_file_name",
                         [
                             ('blue_cross_nc_sample.txt', 'blue_cross_nc_sample.csv'),
                             ('emedny_sample.txt', 'emedny_sample.csv'),
                             ('united_healthcare_legacy_sample.txt', 'united_healthcare_legacy_sample.csv')
                         ])
def test_cli(tmp_path: pathlib.Path,
             test_input_directory: str,
             test_output_directory: str,
             edi_file_name: str,
             csv_file_name: str):
    """
    Tests the edi-835 parser using the cli "main" function.

    :param tmp_path: Pytest fixture used to provide "temp" directories with test cases.
    :param test_input_directory: The test_input_directory fixture defined in conftest.
    :param test_output_directory: The test_output_directory fixture defined in conftest.
    :param edi_file_name: The input edi file name used in the test case.
    :param csv_file_name: The output csv file name used to compare results for the test case.
    """
    # run main cli function
    actual_file = f'{tmp_path.as_posix()}/{csv_file_name}'
    args = [
        f'{test_input_directory}/{edi_file_name}',
        actual_file
    ]
    main(args)

    expected_file = f'{test_output_directory}/{csv_file_name}'
    expected_df: DataFrame = read_csv(expected_file, index_col=0)

    actual_df: DataFrame = read_csv(actual_file, index_col=0)
    pandas.testing.assert_frame_equal(expected_df, actual_df)
