from pydantic import BaseModel


class SUserAuth(BaseModel):
    username: str
    password: str

    # class Config:
    #     orm_mode = True


class SUserInfo(BaseModel):
    username: str
    code: str
    count_changes: int


class SFriendUserInfo(BaseModel):
    username: str
    code: str


class SMyFriendUserInfo(BaseModel):
    id: int
    username: str
