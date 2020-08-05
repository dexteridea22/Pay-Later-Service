from .users import User
from Simpl.models.exceptions import InsufficientCreditException, InvalidAmountValue
from Simpl.models.exceptions import InvalidCreditLimit


# whether credit limit required to define setter or getter ???
# made read only credit limit and dues only getters allowed
# validations and logics of updating limit and dues on simpl side
# just provide a api to user


class Customer(User):
    """
    Handle Customer data initialization
    """
    instances = {}

    def __init__(self, name: str, email_id: str, credit_limit: int):
        super().__init__(name=name, email=email_id)
        Customer.instances[name] = self
        self.credit_limit = credit_limit
        self._remaining_credit = int(credit_limit)

    @property
    def credit_limit(self):
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, limit: int):
        limit = int(limit)
        if limit < 0:
            raise InvalidCreditLimit("credit limit cannot be negative")
        elif limit > 10000:
            raise InvalidCreditLimit("credit limit beyond specified limit")
        self._credit_limit = limit

    def payback(self, amount: float):
        try:
            if float(amount) < 0:
                raise InvalidAmountValue("Amount cannot be negative")
            self._remaining_credit += int(amount)
        except InvalidAmountValue as e:
            raise InvalidAmountValue("Amount cannot be negative")

    def use_credit(self, amount: float):
        if self._remaining_credit < amount:
            raise InsufficientCreditException(
                f"Amount {amount} exceeds the remaining credit limit: {self._remaining_credit}"
            )
        self._remaining_credit -= amount
        return True

    def get_user_dues(self):
        return int(self.credit_limit) - int(self._remaining_credit)
