from ..cmd import Cmd
from Simpl.models.customers import Customer
from Simpl.models.exceptions import InvalidCustomerException


class Cmdnewuser(Cmd):

    def process(self, name, email_id, credit_limit) -> None:

        if not Customer.instances.get(name):
            try:
                Customer(name, email_id, credit_limit)
                print("new user created")
            except KeyError as k:
                raise Exception(k.args)
            except Exception:
                del Customer.instances[name]
                raise
        else:
            raise InvalidCustomerException("User already exists")
