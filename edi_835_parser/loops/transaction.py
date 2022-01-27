from typing import Iterator, Tuple, Optional, List
from warnings import warn

from edi_835_parser.loops.claim import Claim as ClaimLoop
from edi_835_parser.loops.organization import Organization as OrganizationLoop
from edi_835_parser.segments.utilities import find_identifier
from edi_835_parser.segments.transaction import Transaction as TransactionSegment


class Transaction:
    initiating_identifier = TransactionSegment.identification
    terminating_identifiers = [
        TransactionSegment.identification,  # TODO: add a comment
        'SE'
    ]

    def __init__(
            self,
            transaction: TransactionSegment = None,
            claims: List[ClaimLoop] = None,
            organizations: List[OrganizationLoop] = None
    ):
        self.transaction = transaction
        self.claims = claims if claims else []
        self.organizations = organizations if organizations else []

    def __repr__(self):
        return '\n'.join(str(item) for item in self.__dict__.items())

    @classmethod
    def build(cls, segment: str, segments: Iterator[str]) -> Tuple['Transaction', Optional[Iterator[str]], Optional[str]]:
        transaction = Transaction()
        transaction.transaction = TransactionSegment(segment)

        segment = segments.__next__()
        while True:
            try:
                if segment is None:
                    segment = segments.__next__()

                identifier = find_identifier(segment)

                if identifier == ClaimLoop.initiating_identifier:
                    claim, segments, segment = ClaimLoop.build(segment, segments)
                    transaction.claims.append(claim)

                elif identifier == OrganizationLoop.initiating_identifier:
                    organization, segments, segment = OrganizationLoop.build(segment, segments)
                    transaction.organizations.append(organization)

                elif identifier in cls.terminating_identifiers:
                    return transaction, segments, segment

                else:
                    segment = None
                    message = f'Identifier: {identifier} not handled in transaction loop.'
                    warn(message)

            except StopIteration:
                return transaction, None, None



