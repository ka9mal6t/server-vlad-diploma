from typing import Optional

from fastapi import APIRouter, Response, Depends
from api.exeptions import UserAlreadyExistException, IncorrectEmailOrPasswordException, AttemptsIsLimitedException, \
    IncorrectCodeException
from api.users.auth import get_password_hash, authenticate_user, create_access_token, generate_new_code
from api.users.dao import UsersDAO
from api.users.dependencies import get_current_user, create_unique_code
from api.users.models import Users
from api.users.schemas import SUserInfo, SUserRegister, SUserLogin
from api.tasks.tasks import send_comfirmation_email

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user_username = await UsersDAO.find_one_or_none(username=user_data.username)
    existing_user_email = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user_email or existing_user_username:
        raise UserAlreadyExistException
    hash_password = get_password_hash(user_data.username, user_data.password)
    code = generate_new_code()
    email_code = await create_unique_code()
    await UsersDAO.add(username=user_data.username,
                       email=user_data.email,
                       hash_pass=hash_password,
                       code=code,
                       email_code=email_code)
    send_comfirmation_email.delay(email_code, user_data.email)



@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.username, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")


@router.get("/info")
async def info_user(current_user: Users = Depends(get_current_user)) -> SUserInfo:
    return current_user


@router.post("/change_code")
async def change_code(current_user: Users = Depends(get_current_user)):
    if current_user.count_changes > 2:
        raise AttemptsIsLimitedException
    await UsersDAO.update_code(current_user.id, current_user.count_changes, generate_new_code())


@router.get("/confirm_email/{code}")
async def confirm_email(code: str) -> Optional[str]:
    user: Users = await UsersDAO.find_one_or_none(email_code=code)
    if user is not None:
        if not user.confirm:
            await UsersDAO.confirm_email(user.id)
            return user.email
    raise IncorrectCodeException
