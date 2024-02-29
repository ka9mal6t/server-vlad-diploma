from sqlalchemy import update

from api.database import async_session_maker
from api.users.models import Users
from api.dao.base import BaseDAO


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def update_code(cls, user_id, count_changes, code):
        async with async_session_maker() as session:
            async with session.begin():
                query = update(cls.model).where(cls.model.id == user_id).values(
                    code=code,
                    count_changes=count_changes+1)
                await session.execute(query)



