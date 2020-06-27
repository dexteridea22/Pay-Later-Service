from .cmd import Cmd
from Simpl.models.customers import Customer
from Simpl.models.exceptions import InvalidCommand
from Simpl.models.exceptions import InvalidAmountValue

class Cmdpay(Cmd):

    def process(self, user, amount):
        try:
            User = Customer.instances[user]
            User.payback(amount)
            print("payback success")
        except KeyError as k:
            raise InvalidCommand("Invalid user")


