from typing import Type
from Simpl.models.exceptions import InvalidCommand


class Dispatcher:

    # _command = {}

    def __init__(self):
        self._command = {}

    def add_command(self, command, handler):
        self._command[command] = handler

    def dispatch(self, command, *args):
        try:
            handler = self._command[command]
        except KeyError as k:
            raise Exception("Invalid keywords")
        try:
            handler().process(*args)
        except TypeError:
            raise InvalidCommand("Missing args")
