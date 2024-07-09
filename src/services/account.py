from schemas.dto.account import AccountDTO
from schemas.dto.transfer import TransferDTO
from schemas.dto.deposit import DepositDTO

from daos.account import AccountDAO
from daos.transfer import TransferDAO
from daos.deposit import DepositDAO

from exceptions.account import (
    AccountAlreadyExistsException,
    AccountNotFoundException,
)

from exceptions.transfer import (
    SameAccountsTransferException,
    InsufficientBalanceException,
) 

# ---------------------------------------------------------- #


def create_an_account(account: AccountDTO) -> AccountDTO:

    if get_account(account.account_number):
        raise AccountAlreadyExistsException()
    
    account_dao = AccountDAO()
    
    return account_dao.create(account)


def make_a_peer_to_peer_transfer(transfer: TransferDTO):

    if transfer.from_ == transfer.to:
        raise SameAccountsTransferException()

    origin_account = get_valid_account(transfer.from_)
    destiny_account = get_valid_account(transfer.to)

    if transfer.amount > origin_account.current_balance:
        raise InsufficientBalanceException()

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


def get_valid_account(account_number: str) -> AccountDTO:
    
    account = get_account(account_number)

    if not account:
        raise AccountNotFoundException(account_number)

    return account


def get_account(account_number: str) -> AccountDTO | None:
    account_dao = AccountDAO()
    
    account = account_dao.read({'account_number': account_number})

    if not len(account):
        return None

    return account[0]


def save_transfer(transfer: TransferDTO) -> TransferDTO:
    transfer_dao = TransferDAO()
    return transfer_dao.create(transfer)


def deposit_into_an_account(account_number: str, deposit: DepositDTO) -> None:
    account = get_valid_account(account_number)
    
    save_deposit(deposit)

    increment_balance(account, deposit.amount)


def save_deposit(deposit: DepositDTO) -> DepositDTO:
    deposit_dao = DepositDAO()
    return deposit_dao.create(deposit)