from sqlalchemy import Column, Integer, String, JSON

from api.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hash_pass = Column(String, nullable=False)
    code = Column(String, nullable=False)
    count_changes = Column(Integer, nullable=False, default=0)
