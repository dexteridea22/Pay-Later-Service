from .cmd import Cmd
from models.merchants import Merchant
from dispatcher import Dispatcher

class Cmdupdate(Cmd):

    def process(self,dsa:str,merchant,discount):
        merchant = Merchant.instances[merchant]
        merchant.discount = discount
        print("updated discount")
