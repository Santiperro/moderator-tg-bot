from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_name: str = "bot_moderator_backend"
    db_username: str = "backend"
    db_password: str = "666"
    db_host: str = "localhost"
    db_port: int = 5433
    db_url: str = (
        f"postgresql+asyncpg://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    print(db_url)
    db_echo: bool = True  # False in production


settings = Settings()
