
from dispatcher import Dispatcher
from commands import Cmdnew, Cmdpay, Cmdreport, Cmdupdate


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
        main_dispatcher.dispatch(command, *args)


if __name__ == "__main__":
    main()
