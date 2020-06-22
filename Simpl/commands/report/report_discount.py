from ..cmd import Cmd
from models.customers import Customer
from models.merchants import Merchant

class Cmdreportdiscount(Cmd):

    def process(self, merchant):

        total_discount = Cmdreportdiscount.get_total_discount(merchant)
        print(f"Discount offered till date {total_discount}")

    @staticmethod
    def get_total_discount(merchant):
        total_discount = 0
        merchant = Merchant.instances.get(merchant)
        discount = merchant.discount
        for cust in Customer.instances:
            user_obj = Customer.instances.get(cust)
            total_discount += (float(user_obj.get_user_dues()) * float(discount))//100
        return total_discount
