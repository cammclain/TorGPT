from __future__ import annotations

from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    super_admin_username: str
    super_admin_password: SecretStr
    database_url: PostgresDsn
    secret_key: SecretStr

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=False)

settings = Settings()
