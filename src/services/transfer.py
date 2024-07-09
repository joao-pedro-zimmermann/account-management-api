from schemas.dto.transfer import TransferDTO

from daos.transfer import TransferDAO


# ---------------------------------------------------------- #


def get_all_transfers() -> list[None] | list[TransferDTO]:
    transfer_dao = TransferDAO()
    return transfer_dao.read()