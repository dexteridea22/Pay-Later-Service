from ..cmd import Cmd
from .report_discount import Cmdreportdiscount
from .report_dues import Cmdreportdues
from .report_user_at_credit_limit import Cmdreportuseratcredit
from .report_total_dues import Cmdreporttotaldues
from Simpl.transmitter import Transmitter

report_transmitter = Transmitter()
report_transmitter.add_command('discount', Cmdreportdiscount)
report_transmitter.add_command('dues', Cmdreportdues)
report_transmitter.add_command('user-at-credit-limit', Cmdreportuseratcredit)
report_transmitter.add_command('total-dues', Cmdreporttotaldues)


class Cmdreport(Cmd):

    def process(self, command, *args):
        try:
            report_transmitter.transmit(command, *args)

        except ValueError:
            raise Exception("Invalid command")
