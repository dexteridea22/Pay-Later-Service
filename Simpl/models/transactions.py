from Simpl.models.exceptions import InvalidTransaction


class Transaction:
    counter = 1
    instances = {}

    def __init__(self, user: str, merchant: str, amount: int):
        self._transaction_id = Transaction.counter
        self._user = user
        self._merchant = merchant
        self._amount = int(amount)
        Transaction.instances[Transaction.counter] = self
        Transaction.counter += 1

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value) -> None:
        if value <= 0:
            raise InvalidTransaction(
                "Amount should not be greater than 0"
            )
        self._amount = value
