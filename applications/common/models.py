from abc import ABC


class User(ABC):

    def __init__(self, name, email_id, contact_phone):
        self.__name = name
        self.__email_id = email_id
        self.__contact_phone = contact_phone


class Account(object):

    def __init__(self, name, email_id, contact_phone, credit_limit):
        self.__name = name
        self.__email_id = email_id
        self.__contact_phone = contact_phone
        self.__credit_limit = credit_limit
        self.__account_status = ACTIVE