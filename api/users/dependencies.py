import random
import string
from datetime import datetime

from fastapi import Request, Depends
import jwt

from api.config import SECRET_KEY, ALGORITHM
from api.exeptions import TokenExpiredTokenException, TokenAbsentException, IncorrectTokenFormatException, \
    UserIsNotExistException
from api.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except Exception as e:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if not expire or int(expire) < datetime.utcnow().timestamp():
        raise TokenExpiredTokenException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotExistException
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserIsNotExistException
    return user


async def create_unique_code(length=100) -> str:
    while True:
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        user = await UsersDAO.find_one_or_none(email_code=random_string)
        if user is None:
            break
    return random_string

