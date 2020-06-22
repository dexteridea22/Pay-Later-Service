from abc import ABC


class User(ABC):
    """
    abstract model for users
    """

    def __init__(self, name, email_id):
        self._name = name
        self._email_id = email_id

