from schemas.dto.transfer import TransferDTO

from daos.base_dao import BaseDao

from src.models.transfer import TransferModel

# ---------------------------------------------------------- #

class TransferDao(BaseDao):

    def __init__(self):
        super().__init__('transfers')

    def create(self, transfer: TransferDTO) -> TransferDTO:
        transfer_model = TransferModel(**transfer.to_dict())
        created_transfer = super().create(transfer_model)
        return TransferDTO(**created_transfer.to_dict())
    
    def read(self, filter: dict | None = None) -> list[TransferDTO] | list[None]:
        db_transfers = super().read(filter)
        return [TransferDTO(**transfer.to_dict()) for transfer in db_transfers]
    
    def update(self, values: dict, filter: dict | None = None):
        return super().update(values, filter)
    
    def delete(self, filter: dict | None = None):
        return super().delete(filter)