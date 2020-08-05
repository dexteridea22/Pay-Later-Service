from ..cmd import Cmd
from Simpl.models.customers import Customer


class Cmdreporttotaldues(Cmd):

    def process(self):
        customer_objects = Customer.instances
        total = 0
        for user_name in customer_objects:
            customer_object = customer_objects[user_name]
            dues = customer_object.get_user_dues()
            print(f"{user_name} : {dues}")
            total += dues
        print(f"total: {total}")

