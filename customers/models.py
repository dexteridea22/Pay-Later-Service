from applications.common.models import User


class Customer(User):

    def __init__(self, name, email_id, contact_phone, credit_limit):
        super().__init__(name, email_id, contact_phone)
        self.__credit_limit = credit_limit



