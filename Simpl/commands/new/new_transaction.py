from ..cmd import Cmd
from Simpl.models.transactions import Transaction
from Simpl.models.transactions import TransactionStatus
from Simpl.models.customers import Customer
from Simpl.models.merchants import Merchant
from Simpl.models.exceptions import InsufficientCreditException,InvalidTransactionAmountException


class Cmdnewtrans(Cmd):

    def process(self, user: str, merchant: str, amount: int):

        user_object = Customer.instances.get(user)
        merchant_object = Merchant.instances.get(merchant)
        if user_object and merchant_object:
            try:
                amount = float(amount)
                Transaction(user, merchant, amount)
                if user_object.use_credit(amount):
                    print("success")
                Transaction.instances[Transaction.counter]._status = TransactionStatus.COMPLETED
            except InsufficientCreditException:
                raise InsufficientCreditException("rejected: reason : Credit Limit")
            except InvalidTransactionAmountException:
                raise
            except Exception:
                del Transaction.instances[Transaction.counter]
                Transaction.counter -= 1
                raise
        else:
            raise Exception("rejected: reason: Invalid user or merchant")
