from .users import User
from Simpl.models.exceptions import InvalidDiscount

# discount read/write allow both getter and setter on Merchant side
class Merchant(User):
    """
    merchant class
    """
    instances = {}

    def __init__(self, name: str, email: str, discount: int):
        super().__init__(name=name, email=email)
        self.discount = discount
        Merchant.instances[name] = self

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value: float):
        value = int(value)
        if value < 0:
            raise InvalidDiscount("Discount value cannot be negative")
        elif value > 100:
            raise InvalidDiscount("Discount percentage cannot exceed 100")
        self._discount = value
