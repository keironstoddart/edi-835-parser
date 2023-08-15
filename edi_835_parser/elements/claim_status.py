from dataclasses import dataclass
from enum import Enum, auto
from warnings import warn


from edi_835_parser.elements import Element


class PayerClassification(Enum):
	PRIMARY = auto()
	SECONDARY = auto()
	TERTIARY = auto()
	UNSPECIFIED = auto()
	UNKNOWN = auto()

	def __str__(self) -> str:
		return str(self.name).lower()


@dataclass
class Status:
	"""
	Attributes:

	- code (:class:`str`): The code provided in the EDI 835 file.
	- description (:class:`str`): The description of the code per `stedi <https://www.stedi.com/edi/x12/segment/CLP>`_.
	- payer_classification (:class:`PayerClassification`)
	"""
	code: str
	description: str
	payer_classification: PayerClassification


_REGISTRY = [
	Status('1', 'processed as primary', PayerClassification.PRIMARY),
	Status('2', 'processed as secondary', PayerClassification.SECONDARY),
	Status('3', 'processed as tertiary', PayerClassification.TERTIARY),
	Status('4', 'denial', PayerClassification.UNSPECIFIED),
	Status('19', 'processed as primary, forwarded to additional payer(s)', PayerClassification.PRIMARY),
	Status('20', 'processed as secondary, forwarded to additional payer(s)', PayerClassification.SECONDARY),
	Status('21', 'processed as tertiary, forwarded to additional payer(s)', PayerClassification.TERTIARY),
	Status('22', 'reversal of previous payment', PayerClassification.UNSPECIFIED),
]


def _lookup_status(code: str) -> Status:
	status = [s for s in _REGISTRY if s.code == code]
	if len(status) == 0:
		warn(f'ClaimStatus: Code {code} does not match a status in the edi-835-parser claim status registry.')
		return Status('code', 'uncategorized', PayerClassification.UNKNOWN)

	return status[0]


class ClaimStatus(Element):

	def parser(self, value: str) -> Status:
		return _lookup_status(value)
