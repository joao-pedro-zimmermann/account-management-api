from models.account import AccountModel
from models.transfer import TransferModel
from models.deposit import DepositModel

# ---------------------------------------------------------- #

def get_in_memory_db():
    return InMemoryDb


class InMemoryDb:

    accounts: list[None] | list[AccountModel] = []
    transfers: list[None] | list[TransferModel] = []
    deposits: list[None] | list[DepositModel] = []
