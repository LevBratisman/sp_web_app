from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.common.model.member import Member


class MemberRepository(CRUDBaseRepository):
    model = Member
