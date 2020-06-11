from Simpl.apps.common.models import User
from Simpl.merchants.models import Merchant
from Simpl.apps.simpl.simpl_layer import Simpl
from datetime import datetime


# whether credit limit required to define setter or getter ???
# made read only credit limit and dues only getters allowed
# validations and logics of updating limit and dues on simpl side
# just provide a api to user
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
        self.__total_dues = 0  # read only
        self.__credit_limit = credit_limit  # read only
        self.__billing_date = datetime.date()  # read only

    @property
    def credit_limit(self):
        print("getter")
        return self._get_credit_limit()

    @property
    def billing_date(self):
        print("getter")
        return self._get_billing_date()

    @property
    def total_dues(self):
        print("getter")
        return self._get_total_dues()

    def _get_credit_limit(self):
        return self.__credit_limit

    def get_billing_date(self):
        return self.__billing_date

    def _get_total_dues(self):
        return self.__total_dues

    def pay_dues_to_simpl(self, amount):
        """
        API to clear dues and pay simpl
        :param amount:
        :return:
        """
        Simpl.pay_dues_to_simpl(self, amount)

    def _make_payment_to_merchant(self, merchant: Merchant, amount):
        """
        API to make payments to merchants
        :param userid:
        :param amount:
        :return:
        """
        Simpl.make_payment_to_merchant(self, merchant, amount)
