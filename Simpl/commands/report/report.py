from ..cmd import Cmd
from .report_discount import Cmdreportdiscount
from .report_dues import Cmdreportdues
from .report_user_at_credit_limit import Cmdreportuseratcredit
from .report_total_dues import Cmdreporttotaldues
from dispatcher import Dispatcher

report_dispatcher = Dispatcher()
report_dispatcher.add_command('discount', Cmdreportdiscount)
report_dispatcher.add_command('dues', Cmdreportdues)
report_dispatcher.add_command('user-at-credit-limit', Cmdreportuseratcredit)
report_dispatcher.add_command('total-dues', Cmdreporttotaldues)


class Cmdreport(Cmd):

    def process(self, command, *args):
        try:
            report_dispatcher.dispatch(command, *args)

        except ValueError:
            raise Exception("Invalid command")
