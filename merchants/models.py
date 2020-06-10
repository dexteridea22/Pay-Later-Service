from applications.common.models import User


class Merchant(User):

    def __init__(self, name, email_id, contact_phone, discount):
        super().__init__(name, email_id, contact_phone)
        self.__discount = discount
