import mock
from Simpl.commands.new.new_customer import Cmdnewuser
from Simpl.commands.payback import Cmdpay
from Simpl.models.customers import Customer
from Simpl.models.exceptions import *


class TestPayback:

    def setup(self):
        self.object_payback = Cmdpay()
        self.cust_obj = Cmdnewuser()
        self.customer = Customer("ra", "sankalp@mac.com", 100)

    @mock.patch("Simpl.models.customers.Customer.payback",
                side_effect=InvalidAmountValue())
    def test_process_negative(self, mock_exceptions):
        # Customer.instances["ra"]._remaining_credit = 100
        try:
            self.object_payback.process("uc", 100)
            assert False
        except InvalidCommand as e:
            assert e.args[0] == 'Invalid user'

    @mock.patch("Simpl.models.customers.Customer.payback",
                side_effect=InvalidAmountValue())
    def test_invalid_payback(self, mock_exceptions):
        # Customer.instances["ra"]._remaining_credit = 100
        try:
            self.object_payback.process("ra", -100)
            assert False
        except InvalidAmountValue as e:
            assert True
