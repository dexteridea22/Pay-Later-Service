class Account(object):
    """

    """

    def __init__(self, username, email_id):
        self._username = username
        self._email_id = email_id
        self._account_status = AccountStatus.ACTIVE