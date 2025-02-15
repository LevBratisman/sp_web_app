from sqlalchemy import update

from app.common.repository.crud_base_repository import CRUDBaseRepository
from app.common.model.post import Post
from app.db.session import async_session_maker
from app.common.model.base import ModelType


class PostRepository(CRUDBaseRepository):
    model = Post


    @classmethod
    async def like(cls, instance_id: int) -> ModelType:
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == instance_id).values(like_count=cls.model.like_count + 1)
            await session.execute(query)
            await session.commit()


    @classmethod
    async def dislike(cls, instance_id: int) -> ModelType:
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == instance_id).values(like_count=cls.model.like_count - 1)
            await session.execute(query)
            await session.commit()