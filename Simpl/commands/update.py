from .cmd import Cmd
from Simpl.models.merchants import Merchant


class Cmdupdate(Cmd):

    def process(self, dsa: str, merchant, discount):
        merchant = Merchant.instances[merchant]
        merchant.discount = discount
        print("updated discount")
