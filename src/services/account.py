from schemas.dto.account import AccountDTO
from schemas.dto.transfer import TransferDTO

from daos.account import AccountDAO
from daos.transfer import TransferDAO

# ---------------------------------------------------------- #


def create_an_account(account: AccountDTO) -> AccountDTO:
    account_dao = AccountDAO()

    if account_dao.read({'account_number': account.account_number}):
        raise Exception('Account already exists')
    
    return account_dao.create(account)


def make_a_peer_to_peer_transfer(transfer: TransferDTO):

    origin_account = get_account(transfer.from_)
    if not origin_account:
        raise Exception('Origin account not found')
    
    destiny_account = get_account(transfer.to)
    if not destiny_account:
        raise Exception('Destiny account not found')
    
    if transfer.amount > origin_account.current_balance:
        raise Exception('Insufficient balance')

    save_transfer(transfer)

    increment_balance(destiny_account, transfer.amount)
    decrement_balance(origin_account, transfer.amount)
    

def increment_balance(account: AccountDTO, amount: int):
    account_dao = AccountDAO()

    account_dao.update(
        {'current_balance': account.current_balance + amount},
        {'account_number': account.account_number}
    )


def decrement_balance(account: AccountDTO, amount: int):
    account_dao = AccountDAO()

    account_dao.update(
        {'current_balance': account.current_balance - amount},
        {'account_number': account.account_number}
    )


def get_account(account_number: str) -> AccountDTO | None:
    account_dao = AccountDAO()
    
    account = account_dao.read({'account_number': account_number})

    return account[0] if len(account) else None


def save_transfer(transfer: TransferDTO) -> TransferDTO:
    transfer_dao = TransferDAO()
    return transfer_dao.create(transfer)