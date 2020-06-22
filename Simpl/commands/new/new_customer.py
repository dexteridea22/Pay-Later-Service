from ..cmd import Cmd
from models.customers import Customer


class Cmdnewuser(Cmd):

    def process(self, name, email_id, credit_limit):
        # print(name)
        # print(email_id)
        # print(credit_limit)
        try:
            if not Customer.instances.get(name):
                Customer(name, email_id, credit_limit)
                print("new user created")
        except ValueError:
            raise Exception("Customer name present")
