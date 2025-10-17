import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from api.config import DATABASE_URL


# нормализуем префикс и добавляем sslmode=require (если нужно)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
if DATABASE_URL and "sslmode=" not in DATABASE_URL:
    DATABASE_URL += ("&" if "?" in DATABASE_URL else "?") + "sslmode=require"

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"ssl": True},   # или SSLContext, если хотите
    pool_pre_ping=True,
    poolclass=NullPool,           # <- с NullPool нельзя pool_timeout
    # echo=True,                  # включите для дебага
)

async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass





