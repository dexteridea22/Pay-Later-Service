from Simpl.transmitter import Transmitter
from Simpl.commands.new.new import Cmdnew
from Simpl.commands.payback import Cmdpay
from Simpl.commands.payback import Cmdpay
from Simpl.commands.update import Cmdupdate
from Simpl.commands.report.report import Cmdreport
from Simpl.models.exceptions import InvalidCommand

main_transmitter = Transmitter()
main_transmitter.add_command('new', Cmdnew)
main_transmitter.add_command('update', Cmdupdate)
main_transmitter.add_command('payback', Cmdpay)
main_transmitter.add_command('report', Cmdreport)


def main():
    while True:
        inp = input("").strip().lower()
        if not inp:
            break
        command, *args = inp.split()
        try:
            main_transmitter.transmit(command, *args)
        except KeyError as k :
            raise Exception("Invalid keywords")
        except InvalidCommand:
            raise InvalidCommand(f"Invalid args to command {command}")


if __name__ == "__main__":
    main()
