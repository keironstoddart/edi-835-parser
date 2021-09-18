# EDI 835 Parser

[![Python - 3.9.0+](https://img.shields.io/badge/Python-3.9.0%2B-orange)](https://www.python.org/downloads/release/python-390/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/keironstoddart/edi-835-parser)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/keironstoddart/edi-835-parser)
[![Downloads](https://pepy.tech/badge/edi-835-parser)](https://pepy.tech/project/edi-835-parser)
[![Downloads](https://pepy.tech/badge/edi-835-parser/month)](https://pepy.tech/project/edi-835-parser)
[![Downloads](https://pepy.tech/badge/edi-835-parser/week)](https://pepy.tech/project/edi-835-parser)

### edi-835-parser: a lightweight EDI 835 file parser

This package provides a simple-to-use Python interface to EDI 835 Health Care Claim Payment and Remittance Advice files.

*This package is made publicly available by [Senscio Systems](https://www.sensciosystems.com/), the company behind the [Ibis Program](https://www.ibisprogram.com/), an industry leading healthcare initiative that helps people take control of their chronic condition management.*

**Please consider taking two minutes to [give feedback](https://og5vg099r1x.typeform.com/to/k49iVBI2).**

### Installation
Binary installers for the latest released version are at the Python Package Index. Please note that you need to run Python 3.9 or higher to install the edi-835-parser.
```
pip install edi-835-parser
```

### Usage
To parse an EDI 835 file simply execute the `parse` function.
```python
from edi_835_parser import parse

path = '~/Desktop/my_edi_file.txt'
transaction_set = parse(path)
```
The `parse` function also works on a directory path.
```python
from edi_835_parser import parse

path = '~/Desktop/my_directory_of_edi_files'
transaction_sets = parse(path)
```
In both cases, `parse` returns an instance of the `TransactionSets` class. 
This is the class you manipulate depending on your needs. 
For example, say you want to work with the transaction sets data as a `pd.DataFrame`.
```python
from edi_835_parser import parse

path = '~/Desktop/my_directory_of_edi_files'
transaction_sets = parse(path)

data = transaction_sets.to_dataframe()
```
And then save that `pd.DataFrame` as a `.csv` file.
```python
data.to_csv('~/Desktop/my_edi_file.csv')
```
The complete set of `TransactionSets` functionality can be found by inspecting the `TransactionSets` 
class found at `edi_parser/transaction_set/transaction_sets.py`

### Tests
Example EDI 835 files can be found in `tests/test_edi_835/files`. To run the tests use `pytest`.
```
python -m pytest
```

### Contributing to edi-835-parser
All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

Not all EDI 835 elements and segments are currently parsable and not all EDI codes are mapped. If you are interested in
contributing to edi-835-parser, please feel free to fork the project and/or reach out by emailing edi835parser@gmail.com.

### Acknowledgements
A special thank you to Github user `gizquier2` for his interest in this project and continued feedback.