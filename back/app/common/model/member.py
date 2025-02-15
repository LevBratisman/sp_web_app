from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped

from app.common.model.base import Base, TimeStampedModel


class Member(Base):
    name: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column()
    class_year: Mapped[Optional[str]] = mapped_column()
    faculty: Mapped[Optional[str]] = mapped_column()
    image_id: Mapped[Optional[str]] = mapped_column()
    major: Mapped[Optional[str]] = mapped_column()
    major_code: Mapped[Optional[str]] = mapped_column()