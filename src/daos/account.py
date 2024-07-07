from schemas.dto.account import AccountDTO

from daos.base_dao import BaseDAO

from models.account import AccountModel

# ---------------------------------------------------------- #

class AccountDAO(BaseDAO):

    def __init__(self):
        super().__init__('accounts')

    def create(self, account: AccountDTO) -> AccountDTO:
        account_model = AccountModel(**account.to_dict())
        created_account = super().create(account_model)
        return AccountDTO(**created_account.to_dict())
    
    def read(self, filter: dict | None = None) -> list[AccountDTO] | list[None]:
        db_accounts = super().read(filter)
        return [AccountDTO(**account.to_dict()) for account in db_accounts]
    
    def update(self, values: dict, filter: dict | None = None):
        return super().update(values, filter)
    
    def delete(self, filter: dict | None = None):
        return super().delete(filter)