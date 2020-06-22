from ..cmd import Cmd
from models.transactions import Transaction


class Cmdreporttotaldues(Cmd):

    def process(self):
        dues = Cmdreporttotaldues.get_total_dues_all()
        print(f"total dues are = {dues}")

    @staticmethod
    def get_total_dues_all():
        dues = 0
        for trans in Transaction.instances.keys():
            dues += Transaction.instances[trans].amount
        return dues
