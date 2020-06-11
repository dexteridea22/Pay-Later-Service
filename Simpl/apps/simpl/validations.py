from Simpl.customers.models import Customer


class Validator(object):

    @staticmethod
    def validate_merchant_pay_amount(user: Customer, amount):
        if amount > user.credit_limit:
            raise ValueError("Amount more than the current limits")
        elif amount < 0:
            raise ValueError("Amount cannot be negative")

    @staticmethod
    def validate_due_amount(user: Customer, amount):
        original_credit_limit = user.credit_limit + user.total_dues
        if amount > original_credit_limit:
            raise ValueError("Due amount too high")
        elif amount < 0:
            raise ValueError("Invalid amount")
