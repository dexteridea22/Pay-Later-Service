from ..cmd import Cmd
from .new_customer import Cmdnewuser
from .new_merchant import Cmdnewmerchant
from .new_transaction import Cmdnewtrans
from Simpl.dispatcher import Dispatcher
from Simpl.models.exceptions import InvalidCommand

new_dispatcher = Dispatcher()
new_dispatcher.add_command('user', Cmdnewuser)
new_dispatcher.add_command('merchant', Cmdnewmerchant)
new_dispatcher.add_command('txn', Cmdnewtrans)


class Cmdnew(Cmd):

    def process(self, command, *args):
        try:
            new_dispatcher.dispatch(command, *args)

        except KeyError as k :
            raise Exception("Invalid keywords")

        except InvalidCommand as e:
            raise InvalidCommand("Invalid arguments to new")
