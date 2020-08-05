from ..cmd import Cmd
from Simpl.models.customers import Customer
from Simpl.models.exceptions import InvalidUserException


class Cmdreportdues(Cmd):

    def process(self, user: str):

        customer = Customer.instances.get(user)
        if customer:
            dues = customer.get_user_dues()
            print(f"Dues of a user is = {float(dues)}")
        else:
            raise InvalidUserException("User not present")