from .users import User
from Simpl.models.exceptions import InvalidAmountValue
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
        Customer.instances[name] = self
        super().__init__(name=name, email=email_id)
        self.credit_limit = credit_limit
        self.remaining_credit = int(credit_limit)

    @property
    def credit_limit(self):
        return self._credit_limit

    @property
    def remaining_credit(self):
        return self._remaining_credit

    @remaining_credit.setter
    def remaining_credit(self, limit: int):
        if limit < 0:
            raise InvalidCreditLimitCreditLimit("credit limit cannot be negative")
        elif limit > 10000:
            raise InvalidCreditLimit("credit limit beyond specified limit")
        self._remaining_credit = limit

    @credit_limit.setter
    def credit_limit(self, limit: int):
        limit = int(limit)
        if limit < 0:
            raise InvalidCreditLimit("credit limit cannot be negative")
        elif limit > 10000:
            raise InvalidCreditLimit("credit limit beyond specified limit")
        self._credit_limit = limit

    def payback(self, amount):
        try:
            if amount < 0:
                raise InvalidAmountValue("Amount cannot be negative")
            self._remaining_credit += int(amount)
        except InvalidAmountValue as e:
            raise InvalidAmountValue("Amount cannot be negative")

    def use_credit(self, amount):
        try:
            if amount < 0:
                raise InvalidAmountValue("Amount cannot be negative")
            self._remaining_credit - int(amount)
        except InvalidAmountValue as e:
            print(e.args)

    def get_user_dues(self):
        return int(self.credit_limit) - int(self._remaining_credit)

    def is_transaction_allowed(self, amount: int):

        if self._remaining_credit >= int(amount):
            return True
        else:
            raise InvalidAmountValue("Amount invalid")
