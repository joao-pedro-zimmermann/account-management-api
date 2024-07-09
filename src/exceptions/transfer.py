class SameAccountsTransferException(Exception):
    def __init__(self):
        super().__init__('The origin account must be different from the destiny account')


class InsufficientBalanceException(Exception):
    def __init__(self):
        super().__init__('Insufficient balance')