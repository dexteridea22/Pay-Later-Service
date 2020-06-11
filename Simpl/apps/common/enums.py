from enum import Enum


class AccountStatus(Enum):
    """

    """
    ACTIVE, INACTIVE, SUSPENDED = 1, 2, 3


class PaymentStatus(Enum):
    """

    """
    SUCCESS, DECLINED, HOLD = 1, 2, 3

