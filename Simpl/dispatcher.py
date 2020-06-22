from typing import Type


class Dispatcher:

    # _command = {}

    def __init__(self):
        self._command = {}

    def add_command(self, command, handler):
        self._command[command] = handler

    def dispatch(self, command, *args):
        handler = self._command[command]
        handler().process(*args)
