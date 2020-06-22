from ..cmd import Cmd
from models.transactions import Transaction
from models.customers import Customer


class Cmdnewtrans(Cmd):

    def process(self, user: str, merchant: str, amount: int):
        try:
            customer = Customer.instances.get(user)
            if customer.is_transaction_allowed(amount):
                Transaction(user, merchant, amount)
                customer.use_credit(amount)
                print("transaction successfull")
        except ValueError:
            raise Exception("Transaction failed due to invalid amount")
