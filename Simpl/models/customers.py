from .users import User


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
        super().__init__(name=name, email_id=email_id)
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
        # if limit < 0:
        #     raise ValueError("credit limit cannot be negative")
        # elif limit > 10000:
        #     raise ValueError("credit limit beyond specified limit")
        self._remaining_credit = limit


    @credit_limit.setter
    def credit_limit(self, limit: int):
        # if limit < 0:
        #     raise ValueError("credit limit cannot be negative")
        # elif limit > 10000:
        #     raise ValueError("credit limit beyond specified limit")
        self._credit_limit = limit

    def payback(self, amount):
        self._remaining_credit += int(amount)

    def use_credit(self, amount):
        self._remaining_credit -= int(amount)
        return

    def get_user_dues(self):
        return int(self.credit_limit) - int(self._remaining_credit)

    def is_transaction_allowed(self, amount: int):
        if self._remaining_credit >= int(amount):
            return True
        else:
            return False
