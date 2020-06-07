from enum import Enum


class Account(object):
    """
    Class for account
    """

    def __init__(self, username, full_name, email_id, contact_phone, account_status):
        self.__username = username
        self.__full_name = full_name
        self.__email_id = email_id
        self.__contact_phone = contact_phone
        self.__account_status = 'Active'

    def _login(self):
        pass


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, UNKNOWN = 1, 2, 3, 4, 5


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8
