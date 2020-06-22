from .users import User


# discount read/write allow both getter and setter on Merchant side
class Merchant(User):
    """
    merchant class
    """
    instances = {}

    def __init__(self, name: str, email_id: str, discount: int):
        Merchant.instances[name] = self
        super().__init__(name=name, email_id=email_id)
        self.discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value: float):
        # if value < 0:
        #     raise ValueError("Discount value cannot be negative")
        # elif value > 100:
        #     raise ValueError("Discount percentage cannot exceed 100 :)")
        self._discount = value
