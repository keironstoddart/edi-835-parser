"""
main.py
The EDI 835 Parser Command Line Interface.
"""

import argparse
import sys
from typing import List
import os
from edi_835_parser import parse

CLI_DESCRIPTION = """
The EDI 835 Parser CLI writes 835 EDI segments to CSV.
"""


def _parse_args(cli_args: List[str] = None):
    """Returns parsed CLI arguments"""
    parser = argparse.ArgumentParser(
        prog="EDI 835 Parser",
        description=CLI_DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument("input_location",
                        help="The path to the input file or directory.",
                        type=str)

    parser.add_argument("csv_output_file",
                        help="The path to csv file output file.",
                        type=str)
    return parser.parse_args(cli_args)


def main(cli_args: List[str] = None):
    """
    CLI module entrypoint
    """
    args = _parse_args(cli_args)

    if not os.path.exists(args.input_location):
        raise FileNotFoundError(f"input location {args.input_location} does not exist")

    output_directory = os.path.dirname(args.csv_output_file)
    if not os.path.exists(output_directory):
        raise FileNotFoundError(f"csv output directory {output_directory} does not exist")

    transaction_sets = parse(args.input_location)
    data = transaction_sets.to_dataframe()
    data.to_csv(args.csv_output_file)


if __name__ == "__main__":
    # parsing system arguments and passing them in so that we can:
    # - bootstrap test cases easily
    # - print help information if no arguments are provided
    system_arguments = sys.argv[1:] if sys.argv else []
    main(system_arguments)
