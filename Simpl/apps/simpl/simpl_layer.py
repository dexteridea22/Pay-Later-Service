from datetime import datetime
from datetime import timedelta
from Simpl.apps.simpl.reporting_layer import Reporting

# handle amount in decimal , how to round off ?
# only simpl has access to update credit limit and dues of user
# Simpl should provide apis to user for making payments to simpl
# Simpl should handle requests of payment to merchant through it
# handle core logic of payments here
from Simpl.customers.models import Customer
from Simpl.merchants.models import Merchant
from Simpl.apps.simpl import validations as Validator


# why static as no instance of class needed ...

class Simpl(object):
    """

    """

    def __init__(self):
        self.__total_discounted_amount = 0
        self.__all_customer_dues = 0

    @property
    def total_discounted_amount(self):
        return self.__total_discounted_amount

    @property
    def all_customer_dues(self):
        return self.__all_customer_dues

    @all_customer_dues.setter
    def all_customer_dues(self, value):
        self.__all_customer_dues = value

    @total_discounted_amount.setter
    def total_discounted_amount(self, value):
        self.__total_discounted_amount = value

    @staticmethod
    def calculate_revised_discount_amount(merchant: Merchant, amount):
        offered_discount = Reporting.get_discount_by_merchant(merchant)
        revised_amount = amount - ((amount * offered_discount) // 100)
        return revised_amount

    @staticmethod
    def make_payment_to_merchant(user: Customer, merchant: Merchant, amount):
        Validator.validate_merchant_pay_amount(user, amount)
        revised_amount = Simpl.calculate_revised_discount_amount(merchant, amount)
        Simpl.update_total_discounted_amount(revised_amount)
        Simpl._increment_total_dues(user, amount)
        Simpl.all_customer_dues += amount
        user.billing_date = Simpl.generate_next_billing_date(user)

    @staticmethod
    def update_total_discounted_amount(amount):
        Simpl.total_discounted_amount += amount

    @staticmethod
    def generate_next_billing_date(self, user : Customer):
        return datetime.now() + timedelta(days=10)

    @staticmethod
    def pay_dues_to_simpl(user: Customer, amount):
        Validator.validate_due_amount(user, amount)
        Simpl._increment_credit_limit(user, amount)
        Simpl._decrement_total_dues(user, amount)

    @staticmethod
    def _increment_credit_limit(user: Customer, amount):
        user.credit_limit += amount

    @staticmethod
    def _decrement_total_dues(user: Customer, amount):
        user.total_dues -= amount

    @staticmethod
    def _increment_total_dues(user: Customer, amount):
        user.total_dues += amount

    # @credit_limit.setter
    # def credit_limit(self, credit_limit):
    #     print("setter")
    #     if MIN_CREDIT_LIMIT > credit_limit or credit_limit > MAX_CREDIT_LIMIT:
    #         raise ValueError("Credit limit too high or too less")
    #     self._set_credit_limit(credit_limit)


class Transaction(object):

    def __init__(self, ):
        pass
