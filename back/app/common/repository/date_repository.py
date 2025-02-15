from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.common.model.date import Date


class DateRepository(CRUDBaseRepository):
    model = Date
