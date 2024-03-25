from typing import Iterator
from src.dto.user import CreateUser
from src.models.user import User
from src.repositories.user import UserRepository
from fastapi import Depends



class UserService:
    def __init__(self, user_repository=Depends(UserRepository)):
        self.user_repository = user_repository

    def get_user(self, user_id) -> User | None:
        return self.user_repository.get_user(user_id)

    def create_user(self, user: CreateUser) -> User:
        return self.user_repository.create_user(User(**user.dict()))

    def get_all_users(self) -> Iterator[User]:
        return self.user_repository.get_all_users()
