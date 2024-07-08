from schemas.dto.deposit import DepositDTO

from daos.base_dao import BaseDAO

from models.deposit import DepositModel

# ---------------------------------------------------------- #

class DepositDAO(BaseDAO):

    def __init__(self):
        super().__init__('deposits')

    def create(self, deposit: DepositDTO) -> DepositDTO:
        deposit_model = DepositModel(**deposit.to_dict())
        created_deposit = super().create(deposit_model)
        return DepositDTO(**created_deposit.to_dict())
    
    def read(self, filter: dict | None = None) -> list[DepositDTO] | list[None]:
        db_deposits = super().read(filter)
        return [DepositDTO(**deposit.to_dict()) for deposit in db_deposits]
    
    def update(self, values: dict, filter: dict | None = None):
        return super().update(values, filter)
    
    def delete(self, filter: dict | None = None):
        return super().delete(filter)