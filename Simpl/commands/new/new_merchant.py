from ..cmd import Cmd
from models.merchants import Merchant


class Cmdnewmerchant(Cmd):

    def process(self, name, email_id, discount):

        if not Merchant.instances.get(name):
            try:
                Merchant(name, email_id, discount)
                print("new merchant created")
            except Exception:
                del Merchant.instances[name]
                raise
        else:
            raise Exception("Merchant name already exist")
