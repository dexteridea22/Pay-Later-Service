from cmd import Cmd
from Simpl.models.customers import Customer


class Cmdreportuseratcredit(Cmd):

    def process(self):
        count = Cmdreportuseratcredit.get_user_at_credit_limit()
        print(f"total users reached credit limit are = {count}")

    @staticmethod
    def get_user_at_credit_limit():
        count = 0
        for cust in Customer.instances.keys():
            if Customer.instances.get(cust)._remaining_credit == 0:
                count += 1
        return count
