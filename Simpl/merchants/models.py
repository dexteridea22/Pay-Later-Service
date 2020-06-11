from Simpl.apps.common.models import User
from Simpl.apps.common.constants import DISCOUNT_MAX_PERCENTAGE


# discount read/write allow both getter and setter on Merchant side
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
        elif discount > DISCOUNT_MAX_PERCENTAGE:
            raise ValueError("Discount percentage cannot exceed 100 :)")
        self.__discount = discount

    def _set_discount(self, discount):
        self.discount = discount

    def _get_discount(self):
        return self.__discount

    def update_discount(self, discount):
        self._set_discount(discount)
