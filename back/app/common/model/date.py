from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Date, Text
from datetime import date
import enum
from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from app.common.model.base import Base, TimeStampedModel


class EventTypeEnum(enum.Enum):
    BIRTHDAY = "BIRTHDAY"
    AWARD = "AWARD"
    DISCOVERY = "DISCOVERY"


class Date(Base):
    event_date: Mapped[date] = mapped_column(Date)
    description: Mapped[Optional[str]] = mapped_column(Text)
    type_of_event: Mapped[str] = mapped_column(
        PgEnum(EventTypeEnum, name="event_type_enum", create_type=False),
        default=EventTypeEnum.BIRTHDAY,
    )
