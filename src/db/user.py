from sqlalchemy import Column, String
from base import Base


class User(Base):
    __tablename__ = "users"

    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
