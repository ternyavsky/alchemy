import dataclasses

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class BaseUser(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: str


class CreateUser(BaseUser):
    pass


class User(BaseUser):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
