from dependency_injector import containers, providers
from src.db.db import Database
from src.repositories.user import UserRepository
from src.services.user import UserService


class Container(containers.DeclarativeContainer):

    db = providers.Singleton(Database)

    user_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session
    )

    user_service = providers.Factory(UserService, user_repository=user_repository)
