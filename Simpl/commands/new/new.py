from ..cmd import Cmd
from .new_customer import Cmdnewuser
from .new_merchant import Cmdnewmerchant
from .new_transaction import Cmdnewtrans
from Simpl.transmitter import Transmitter
from Simpl.models.exceptions import InvalidCommand

new_transmitter= Transmitter()
new_transmitter.add_command('user', Cmdnewuser)
new_transmitter.add_command('merchant', Cmdnewmerchant)
new_transmitter.add_command('txn', Cmdnewtrans)


class Cmdnew(Cmd):

    def process(self, command, *args):
        try:
            new_transmitter.transmit(command, *args)

        except KeyError as k:
            raise Exception("Invalid keywords")

        except InvalidCommand as e:
            raise InvalidCommand("Invalid arguments to new")
