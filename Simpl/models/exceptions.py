class CommandExeption(Exception):
    pass


class ModelException(Exception):
    pass


class ModelCustomerException(ModelException):
    pass


class ModelMerchantException(ModelException):
    pass


class ModelTransactionException(ModelException):
    pass


class InvalidCustomerException(ModelCustomerException):
    pass


class NameException(ModelException):
    pass


class EmailException(ModelException):
    pass


class InvalidMerchantException(ModelMerchantException):
    pass


class InvalidCreditLimit(ModelCustomerException):
    pass


class InvalidCreditLimit(ModelCustomerException):
    pass


class InvalidDiscount(ModelMerchantException):
    pass


class InvalidCommand(CommandExeption):
    pass


class InvalidAmountValue(ModelCustomerException):
    pass


class InvalidTransaction(ModelTransactionException):
    pass

class InvalidDiscount(ModelMerchantException):
    pass