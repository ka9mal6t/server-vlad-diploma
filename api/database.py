from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from api.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,                 # уже содержит ?sslmode=require
    connect_args={"ssl": True},   # asyncpg сам создаст SSLContext
    pool_pre_ping=True,           # проверка соединения перед запросом
    poolclass=NullPool,           # не держим «мертвые» коннекты
    pool_timeout=30,
)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


