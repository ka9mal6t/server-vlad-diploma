from sqlalchemy import Column, Integer, String, JSON, Boolean

from api.database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    email_code = Column(String(100), unique=True, nullable=False)
    confirm = Column(Boolean, nullable=False, default=False)
    hash_pass = Column(String, nullable=False)
    code = Column(String, nullable=False)
    count_changes = Column(Integer, nullable=False, default=0)
