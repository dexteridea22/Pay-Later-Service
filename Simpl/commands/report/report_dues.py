from ..cmd import Cmd
from Simpl.models.customers import Customer


class Cmdreportdues(Cmd):

    def process(self, user: str):
        customer = Customer.instances[user]
        dues = customer.get_user_dues()
        print(f"Dues of a user is = {dues}")
