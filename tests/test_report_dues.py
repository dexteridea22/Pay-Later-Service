import mock
from Simpl.commands.report.report_dues import Cmdreportdues
from Simpl.models.exceptions import InvalidUserException


class TestReportTotalDues:
    def setup(self):
        self.report_dues = Cmdreportdues()

    def test_process(self):
        try:
            self.report_dues.process("rb")
        except InvalidUserException as e:
            assert e.args[0] == "User not present"

    @mock.patch("Simpl.models.customers.Customer.get_user_dues", return_values=100.0)
    def test_process_all(self, mock_user_instance):
        self.report_dues.process("ra") is None

