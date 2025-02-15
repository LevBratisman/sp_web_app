from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import settings


async_engine = create_async_engine(
    settings.POSTGRES_DATABASE_URI, pool_pre_ping=True
)

async_session_maker = async_sessionmaker(
        bind=async_engine, 
        expire_on_commit=False, 
        autoflush=False,
    )