from applications.common.models import User
from applications.common.constants import (
    MIN_CREDIT_LIMIT, MAX_CREDIT_LIMIT)


class Guest(User):
    """

    """

    def register_account(self):
        pass


class Customer(User):
    """

    """

    def __init__(self, name, email_id, contact_phone, credit_limit):
        super().__init__(name, email_id, contact_phone)
        self.__total_due = 0
        self.credit_limit = credit_limit

    @property
    def credit_limit(self):
        print("getter")
        return self._get_credit_limit()

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        print("setter")
        if MIN_CREDIT_LIMIT > credit_limit or credit_limit > MAX_CREDIT_LIMIT:
            raise ValueError("Credit limit too high or too less")
        self._set_credit_limit(credit_limit)

    def _get_credit_limit(self):
        return self.__credit_limit

    def _set_credit_limit(self, credit_limit):
        self.__credit_limit = credit_limit

    def pay_dues_to_simpl(self, amount):
        self._make_payment(amount)
        pass

    def _make_payment(self, amount):
        self._validate_amount(amount)
        self.update_credit_limit(amount)
        self.update_total_dues(amount)
        pass

    def _validate_amount(self, amount):
        if amount > self.__credit_limit:
            raise Exception("Amount more than the current limits")

    def update_credit_limit(self, amount):
        self._set_credit_limit(self.__credit_limit - amount)

    def update_total_dues(self, amount):
        self.__total_due += amount
