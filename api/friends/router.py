from fastapi import APIRouter, Depends
from api.exeptions import UserIsNotFoundException, FriendAlreadyExistException
from api.friends.dao import FriendsDAO
from api.users.dao import UsersDAO
from api.users.dependencies import get_current_user
from api.users.models import Users
from api.users.schemas import SFriendUserInfo, SMyFriendUserInfo
from api.users.utils import decrypt_code

router = APIRouter(
    prefix="/friends",
    tags=["Friends"]
)


@router.get("/get_friends")
async def get_friends(current_user: Users = Depends(get_current_user)) -> list[SFriendUserInfo]:
    friends = await FriendsDAO.find_all(friend_id=current_user.id)
    if not friends:
        return friends
    users_friends = []
    for friend in friends:
        friend_info = await UsersDAO.find_one_or_none(id=friend.owner_id)
        friend_info.code = decrypt_code(friend_info.code)
        users_friends.append(friend_info)
    return users_friends


@router.get("/get_my_friends")
async def get_my_friends(current_user: Users = Depends(get_current_user)) -> list[SMyFriendUserInfo]:
    friends = await FriendsDAO.find_all(owner_id=current_user.id)
    if not friends:
        return friends
    users_friends = []
    for friend in friends:
        users_friends.append(await UsersDAO.find_one_or_none(id=friend.friend_id))
    return users_friends


@router.post("/add_friend")
async def add_friend(username: str, current_user: Users = Depends(get_current_user)):
    user = await UsersDAO.find_one_or_none(username=username)
    if not user or user.id == current_user.id:
        raise UserIsNotFoundException
    check = await FriendsDAO.find_one_or_none(owner_id=current_user.id, friend_id=user.id)
    if check:
        raise FriendAlreadyExistException

    await FriendsDAO.add(owner_id=current_user.id, friend_id=user.id)


@router.delete("/delete_friend/{id}", status_code=204)
async def delete_friend(id: int, current_user: Users = Depends(get_current_user)):
    user = await UsersDAO.find_one_or_none(id=id)
    if not user:
        raise UserIsNotFoundException
    await FriendsDAO.delete(owner_id=current_user.id, friend_id=user.id)
