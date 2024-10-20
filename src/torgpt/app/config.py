from __future__ import annotations

from pydantic_settings import BaseSettings

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    super_admin_username: str
    super_admin_password: str
    database_url: str
    secret_key: str
