import mock
from Simpl.commands.new.new_merchant import Cmdnewmerchant
from Simpl.models.merchants import Merchant
from Simpl.models.exceptions import EmailException, NameException
from Simpl.models.exceptions import *


class TestNewMerchant:
    def setup(self):
        self.object_new_user = Cmdnewmerchant()
        self.new_merchant = Merchant("sankalp", "ssankalp@google.com", 10)

    def test_merchant_discount_negative(self):
        try:
            Merchant("sanalp", "ssa@fsasa.com", -1)
            assert False
        except InvalidDiscount as e:
            print(e.args)
            assert e.args[0] == "Discount value cannot be negative"

    def test_merchant_process_high(self):
        try:
            Merchant("sanalp", "ssa@fsasa.com", 1000)
            assert False
        except InvalidDiscount as e:
            print(e.args)
            assert e.args[0] == "Discount percentage cannot exceed 100"