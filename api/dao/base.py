from sqlalchemy import select, insert, delete
from api.database import async_session_maker, engine


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            # print(query.compile(engine, compile_kwargs={"literal_binds": True}))
            return result.scalars().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **params):
        async with (async_session_maker() as session):
            query = delete(cls.model).where(*[getattr(cls.model, key) == value for key, value in params.items()])
            await session.execute(query)
            await session.commit()
