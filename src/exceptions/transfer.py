class SameAccountsTransferException(Exception):
    def __init__(self):
        super().__init__('Transfer to the same account is not allowed. Please select a different destination account')


class InsufficientBalanceException(Exception):
    def __init__(self):
        super().__init__('Insufficient balance')