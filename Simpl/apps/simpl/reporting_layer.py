from Simpl.customers.models import Customer
from Simpl.merchants.models import Merchant
from Simpl.apps.simpl.simpl_layer import Simpl


class Reporting(object):

    @staticmethod
    def get_total_customer_dues():
        return Simpl.all_customer_dues

    @staticmethod
    def get_total_discounts():
        return Simpl.total_discounted_amount

    @staticmethod
    def get_dues_by_user(user: Customer):
        return Customer.total_dues

    @staticmethod
    def get_discount_by_merchant(merchant: Merchant):
        return Merchant.discount

    def get_users_with_full_usage_credit_limit():
        pass
