import os, ssl
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool  # важно

DATABASE_URL = os.getenv("DATABASE_URL")  # полный URL от Render, НЕ собирать руками!
if DATABASE_URL and "sslmode=" not in DATABASE_URL:
    DATABASE_URL += ("&" if "?" in DATABASE_URL else "?") + "sslmode=require"

# Вариант 1 (проще): ssl=True — asyncpg сам создаст контекст
engine = create_async_engine(
    DATABASE_URL,
    connect_args={"ssl": True},
    pool_pre_ping=True,          # проверяем коннект перед использованием
    poolclass=NullPool,          # без пула — нет «протухших» соединений
)

async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


