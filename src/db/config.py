class Settings:
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: int
    DB_PORT: int

    @property
    def DATABASE_URL(self) -> str:
        return "sqlite:///champ.db"


settings = Settings()
