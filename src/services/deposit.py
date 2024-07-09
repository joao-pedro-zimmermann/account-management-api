from schemas.dto.deposit import DepositDTO

from daos.deposit import DepositDAO


# ---------------------------------------------------------- #


def get_all_deposits() -> list[None] | list[DepositDTO]:
    transfer_dao = DepositDAO()
    return transfer_dao.read()