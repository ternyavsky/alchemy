from sqlalchemy.types import Text
from src.db.base import Base
from sqlalchemy import Column, LargeBinary, String, Integer


class User(Base):
    __tablename__ = "users"
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    email = Column(String)
    # qr_code = Column(Text)
