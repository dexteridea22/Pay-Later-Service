from Simpl.models.exceptions import InvalidTransactionAmountException
from enum import IntEnum

class TransactionStatus(IntEnum):
    PENDING = 0
    COMPLETED = 1
    BLOCKED = 2


class Transaction:
    counter = 0
    instances = {}

    def __init__(self, user: str, merchant: str, amount: float):
        self._transaction_id = Transaction.counter
        self._user = user
        self._merchant = merchant
        self._status = TransactionStatus.PENDING
        self.amount = float(amount)
        Transaction.counter += 1
        Transaction.instances[Transaction.counter] = self

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value) -> None:
        if value <= 0:
            raise InvalidTransactionAmountException(
                "Amount should be greater than 0"
            )
        self._amount = value
