from schemas.dto.account import AccountDTO

from daos.account import AccountDao

# ---------------------------------------------------------- #

def create_an_account(account_to_create: AccountDTO) -> AccountDTO:
    account_dao = AccountDao()

    if account_dao.read({'account_number': account_to_create.account_number}):
        raise Exception('Account already exists')
    
    return account_dao.create(account_to_create)