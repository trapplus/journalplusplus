from pydantic import computed_field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: str = ""  # loaded from .env, wo default value
    LOG_LEVEL: str = "INFO"
    DB_TYPE: str = "sqlite"
    DB_URL: str = "sqlite:///./database.db"

    @computed_field
    @property
    def database_url(self) -> str:

        allowed = {"sqlite", "postgres", "mysql"}
        if self.DB_TYPE not in allowed:
            raise ValueError(f"DB_TYPE must be one of {allowed}")
        return self.DB_URL

    class Config:
        env_file = ".env"


config = Config()
