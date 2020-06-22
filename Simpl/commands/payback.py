from .cmd import Cmd
from models.customers import Customer


class Cmdpay(Cmd):

    def process(self, user, amount):
        User = Customer.instances[user]
        User.payback(amount)
        print("payback success")
