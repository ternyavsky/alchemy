from typing import Callable
from sqlalchemy import create_engine, orm
from src.db.config import settings
from src.db.base import Base
from contextlib import AbstractContextManager, contextmanager


class Database:
    def __init__(self):
        self.engine = create_engine(
            url=settings.DATABASE_URL,
            echo=True,
        )
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        )

    def init_db(self):
        Base.metadata.create_all(bind=self.engine)


