from ..cmd import Cmd
from Simpl.models.transactions import Transaction
from Simpl.models.customers import Customer
from Simpl.models.exceptions import *


class Cmdnewtrans(Cmd):

    def process(self, user: str, merchant: str, amount: int):
        customer = Customer.instances.get(user)
        try:
            customer.is_transaction_allowed(amount)
            Transaction(user, merchant, amount)
            customer.use_credit(amount)
        except InvalidTransaction:
            raise InvalidTransaction(
                "Invalid amount,Either Amount negative or higher then credit limit")
