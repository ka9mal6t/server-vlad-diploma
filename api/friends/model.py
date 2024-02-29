from sqlalchemy import Integer, Column, ForeignKey

from api.database import Base


class Friends(Base):
    __tablename__ = 'friends'

    id = Column(Integer, primary_key=True)
    owner_id = Column(ForeignKey('users.id'), nullable=False)
    friend_id = Column(ForeignKey('users.id'), nullable=False)
