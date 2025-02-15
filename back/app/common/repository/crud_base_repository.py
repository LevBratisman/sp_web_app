from abc import ABC, abstractmethod

from sqlalchemy import select, insert, update, delete

from app.common.model.base import ModelType
from app.db.session import async_session_maker


class AbstractRepository(ABC):
    """
    Interface for all repositories
    """
    @abstractmethod
    async def add():
        raise NotImplementedError

    @abstractmethod
    async def get_one():
        raise NotImplementedError

    @abstractmethod
    async def get_by_id():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError

    @abstractmethod
    async def delete():
        raise NotImplementedError



class CRUDBaseRepository(AbstractRepository):
    model: ModelType = None

    @classmethod
    async def get_one(cls, **filters) -> ModelType:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = await session.execute(query)

            return result.scalar_one_or_none()


    @classmethod
    async def get_by_id(cls, *, instance_id: int) -> ModelType:
        async with async_session_maker() as session:
            query = select(cls.model).where(cls.model.id == instance_id)
            result = await session.execute(query)

            return result.scalar_one_or_none()


    @classmethod
    async def get_all(cls, **filters) -> list[ModelType]:
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filters)
            result = await session.execute(query)

            return result.scalars().all()
    

    @classmethod
    async def add(cls, **data) -> ModelType:
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(query)
            await session.commit()

            return result.scalar_one_or_none()
        

    @classmethod
    async def update(cls, data) -> ModelType:
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == data['id']).values(**data).returning(cls.model)
            await session.execute(query)
            await session.commit()


    @classmethod
    async def delete(cls, *, instance_id: int) -> ModelType:
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == instance_id)
            await session.execute(query)
            await session.commit()
