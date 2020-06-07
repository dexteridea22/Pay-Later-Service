from enum_data_types import Account
from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self,account :Account):


class Guest(User):

    def register_account(self):
        """
        Allow guest user to register an account
        :return:
        """




class Customer(User):

    def __init__(self,full_name, email_id, contact_phone,credit_limit):
        super().__init__(full_name, email_id, contact_phone)
        self.__credit_limit = credit_limit
        self.__total_dues = 0
        self.__due_date = 0


    def _make_payment(self,amount,merchant_id,payment_mode):
       """
       :param amount:
       :param merchant_id:
       :return:
       """
        if self.__credit_limit - self.__total_dues > amount  :
            self.__total_dues += amount
        else :
            raise Exception("CREDIT LIMIT OVERFLOW")


    def _clear_dues_of_simpl(self,payment_mode:Payment):
        """
        clear dues of the simpl before due date
        :return:
        """
        self.__total_dues = 0





class Merchant(User):


    def __init__(self,full_name, email_id, contact_phone,discount):
        super(Merchant, self).__init__(full_name, email_id, contact_phone)
        self.__offered_discount = discount

    def _update_discounts(self,discount):
        """
        change the discount offered to simpl
        :return:
        """
        self.__offered_discount = discount




class Simpl(payment):

    _user_list = []


    def make_payment_to_merchant(self,amount,merchant_id,user_id):
        """
        :param amount:
        :param merchant_id:
        :param user_id:
        :return:
        """

    def  _get_dues_by_user(self,user_id):
        """
        get dues by a particular user
        :param user_id:
        :return:
        """


    def  _get_discount_by_merchant(self,merchant_id):
        """
        get discount rate offered
        :param merchant_id:
        :return:
        """


    def  _check_credit_limit(self,user_id):
        """
        check user credit limit , raise
        :param user_id:
        :return:
        """

    def _update_credit_limit(self, user_id,credit_limit):
        """
        check user credit limit
        :param user_id:
        :return:
        """

    def _generate_due_end_date(self,user_id):
        """
        generate users cycle date for a billing
        :return:
        """


    def _calculate_dues(self,user_id):
        """
        calculate user amount tracking all transactions
        :param user_id:
        :return:
        """

    def send_notification(self):


class Notification(object):
    pass













