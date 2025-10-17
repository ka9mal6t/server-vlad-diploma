from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

import ssl

from api.config import DATABASE_URL

engine = create_async_engine(
    DATABASE_URL,
    connect_args={"ssl": ssl_context})

async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass

