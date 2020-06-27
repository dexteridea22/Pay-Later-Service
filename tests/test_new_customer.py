import mock
from Simpl.commands.new.new_customer import Cmdnewuser
from Simpl.models.customers import Customer
from Simpl.models.exceptions import EmailException, NameException
from Simpl.models.exceptions import *


class TestNewCustomer:
    def setup(self):
        self.object_new_user = Cmdnewuser()
        self.new_customer_email = Customer("sankalp", "ssankalp@google.com", 1000)

    # @mock.patch("Simpl.models.customers.Customer", return_value=None)
    def test_process_invalid(self):
        try:
            self.object_new_user.process("ubsa", "ub@gmail.com")
            assert False
        except TypeError as e:
            assert e.args[0] == "process() missing 1 required positional argument: 'credit_limit'"

    def test_customer_email(self):
        new_customer = Customer("sankalp", "sankalp@google.com", 1000)
        assert new_customer.email == "sankalp@google.com"

    def test_customer_invalid_mail(self):
        try:
            Customer("sanalp", "s@f.com", 100)
            assert False
        except EmailException as e:
            # print(e.args)
            assert e.args[
                       0] == "Email format invalid. Expected: [<more_than_two_letter>@<more_than_three_letter>.<not_more_than_two_to_three_letter>]+(*All in small case)"

    def test_customer_invalid_name(self):
        try:
            Customer("san1alp", "s@f.com", 100)
            assert False
        except NameException as e:
            print(e.args)
            assert e.args[0] == "Name format invalid: name may only consist of letter"

