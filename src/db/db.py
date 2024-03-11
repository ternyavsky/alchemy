from sqlalchemy import create_engine
from config import settings
from base import Base

from user import User

engine = create_engine(
    url=settings.DATABASE_URL, echo=True, pool_size=5, max_overflow=10
)

engine.connect()

Base.metadata.create_all(bind=engine)
