import ssl
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase   
from sqlalchemy.pool import NullPool

from api.config import DATABASE_URL

ssl_ctx = ssl.create_default_context()


# нормализуем префикс и добавляем sslmode=require (если нужно)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_async_engine(
    DATABASE_URL,                      # БЕЗ ?sslmode=...
    connect_args={
        "ssl": ssl_ctx,                # TLS
        "statement_cache_size": 0,     # ключевой фикс для PgBouncer
        # "timeout": 30.0,             # (опц.) таймаут на установку соединения
    },
    pool_pre_ping=True,
    poolclass=NullPool,                # на Render самое стабильное
    # echo=True,
)

async_session_maker = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass









