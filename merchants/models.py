from applications.common.models import User


class Merchant(User):
    """

    """

    def __init__(self, name, email_id, contact_phone, discount):
        super().__init__(name, email_id, contact_phone)
        self._set_discount(discount)

    @property
    def discount(self):
        print("getter")
        return self._get_discount()

    @discount.setter
    def discount(self, discount):
        print("setter")
        if discount < 0:
            raise ValueError("Discount value cannot be negative")
        self.__discount = discount

    def _set_discount(self, discount):
        self.discount = discount

    def _get_discount(self):
        return self.__discount

    def update_discount(self, discount):
        self._set_discount(discount)
