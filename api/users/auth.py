import hashlib
import random
from datetime import datetime, timedelta

import jwt

from api.config import SECRET_KEY, ALGORITHM
from api.users.dao import UsersDAO


def get_password_hash(username: str, password: str) -> str:
    return hashlib.sha256((username + password).encode('utf-8')).hexdigest()


def generate_new_code() -> str:
    numbers = []
    while len(numbers) < 5:
        el = random.randint(10, 99)
        if str(el) not in numbers:
            numbers.append(str(el))
    return ''.join(numbers)


def verify_password(username: str, plain_password: str, hashed_password: str) -> bool:
    return hashlib.sha256((username + plain_password).encode('utf-8')).hexdigest() == hashed_password


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encode_jwt


async def authenticate_user(username: str, password: str):
    user = await UsersDAO.find_one_or_none(username=username, confirm=True)
    if not user or not verify_password(username, password, user.hash_pass):
        return None
    return user
