from Simpl.dispatcher import Dispatcher
from Simpl.commands.new.new import Cmdnew
from Simpl.commands.payback import Cmdpay
from Simpl.commands.payback import Cmdpay
from Simpl.commands.update import Cmdupdate
from Simpl.commands.report.report import Cmdreport
from Simpl.models.exceptions import InvalidCommand

main_dispatcher = Dispatcher()
main_dispatcher.add_command('new', Cmdnew)
main_dispatcher.add_command('update', Cmdupdate)
main_dispatcher.add_command('payback', Cmdpay)
main_dispatcher.add_command('report', Cmdreport)


def main():
    while True:
        inp = input("").strip().lower()
        if not inp:
            break
        command, *args = inp.split()
        try:
            main_dispatcher.dispatch(command, *args)
        except KeyError as k :
            raise Exception("Invalid keywords")
        except InvalidCommand:
            raise InvalidCommand(f"Invalid args to command {command}")


if __name__ == "__main__":
    main()
