from datetime import date
from app.common.dto.base import BaseDTO, IdBase
from app.common.model.date import EventTypeEnum


class Date(BaseDTO):
    event_date: date
    description: str
    type_of_event: EventTypeEnum


class DateAddDTO(Date):
    pass


class DateUpdateDTO(IdBase):
    event_date: date | None
    description: str | None
    type_of_event: EventTypeEnum | None


class DateDTO(Date, IdBase):
    pass
