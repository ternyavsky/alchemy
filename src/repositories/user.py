from typing import Callable, Iterator
from contextlib import AbstractContextManager
from sqlalchemy import orm
from src.models.user import User
from src.db.db import Database
from fastapi import Depends

def get_session() -> Callable[..., AbstractContextManager[orm.Session]]:
    session: orm.Session = Database()._session_factory
    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

class UserRepository:
    def __init__(
        self, session_factory=Depends(get_session)
    ):
        self.session_factory = session_factory
        print("SESSION FAC")

    def get_user(self, user_id) -> User | None:
        with self.session_factory() as session:
            return session.query(User).filter(User.id == user_id).first()

    def create_user(self, user: User) -> User:
        with self.session_factory() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def get_all_users(self) -> Iterator[User]:
        with self.session_factory() as session:
            return session.query(User).all()
