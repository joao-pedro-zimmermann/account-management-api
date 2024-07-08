class AccountNotFoundException(Exception):
    def __init__(self, account_number: str):
        super().__init__(f'Account {account_number} not found')


class InsufficientBalanceException(Exception):
    def __init__(self):
        super().__init__(f'Insufficient balance')


class AccountAlreadyExistsException(Exception):
    def __init__(self):
        super().__init__('Account already exists')