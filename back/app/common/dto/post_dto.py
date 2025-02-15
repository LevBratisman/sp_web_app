from app.common.dto.base import BaseDTO, IdBase, TimeStampedBase


class Post(TimeStampedBase):
    description: str
    like_count: int | None
    title: str | None
    image_id: str | None


class PostAddDTO(BaseDTO):
    description: str
    title: str | None
    image_id: str | None


class PostUpdateDTO(IdBase):
    description: str
    title: str | None
    image_id: str | None


class PostDTO(Post, IdBase):
    pass