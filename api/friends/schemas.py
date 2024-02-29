from pydantic import BaseModel


class SFriend(BaseModel):
    owner_id: int
    friend_id: int

    # class Config:
    #     orm_mode = True
