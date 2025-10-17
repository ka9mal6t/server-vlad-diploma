from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from api.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"ssl": True},
    pool_pre_ping=True,
    poolclass=QueuePool,     # пул
    pool_size=5,             # подберите под лимиты БД
    max_overflow=0,          # чтобы не превысить лимит
    pool_timeout=30,         # теперь допустим
)

async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass



