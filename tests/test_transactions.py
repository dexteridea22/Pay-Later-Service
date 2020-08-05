import mock
from Simpl.commands.new.new_customer import Cmdnewuser
from Simpl.commands.new.new_transaction import Cmdnewtrans
from Simpl.models.customers import Customer
from Simpl.models.merchants import Merchant
from Simpl.models.exceptions import *


class TestTransaction:

    def setup(self):
        self.customer = Customer("usa", "saxs@dsds.com", 100)
        self.merchant = Merchant("mer", "dss@dsds.com", 10)
        self.trans_obj = Cmdnewtrans()

    @mock.patch("Simpl.models.customers.Customer",
                side_effect=InsufficientCreditException())
    def test_transaction_invalid_amount(self, mock_exceptions):
        try:
            self.trans_obj.process("usa", "mer", 120)
            assert False
        except InsufficientCreditException as e:
            assert e.args[0] == "rejected: reason : Credit Limit"

    @mock.patch("Simpl.models.customers.Customer.use_credit",
                side_effect=InvalidTransactionAmountException())
    def test_transaction_negative_amount(self, mock_exceptions):
        try:
            self.trans_obj.process("usa", "mer", -120)
            assert False
        except InvalidTransactionAmountException as e:
            assert e.args[0] == "Amount should be greater than 0"
