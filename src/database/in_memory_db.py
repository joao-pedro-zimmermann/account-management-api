from models.account import AccountModel

# ---------------------------------------------------------- #

def get_in_memory_db():
    return InMemoryDb


class InMemoryDb:

    accounts: list[None] | list[AccountModel] = []
