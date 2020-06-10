from abc import ABC
from applications.common.enums import AccountStatus


class User(ABC):
    """

    """

    def __init__(self, name, email_id, contact_phone):
        self.__name = name
        self.__email_id = email_id
        self.__contact_phone = contact_phone

    def login(self):
        pass

    def register_account(self):
        pass


class Account(object):
    """

    """

    def __init__(self, username, email_id, contact_phone):
        self.__username = username
        self.__email_id = email_id
        self.__contact_phone = contact_phone
        self.__account_status = AccountStatus.ACTIVE
