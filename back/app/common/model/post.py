from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional

from app.common.model.base import Base, TimeStampedModel


class Post(Base, TimeStampedModel):
    title: Mapped[Optional[str]] = mapped_column()
    description: Mapped[str] = mapped_column()
    image_id: Mapped[Optional[str]] = mapped_column()
    like_count: Mapped[int] = mapped_column(default=0)