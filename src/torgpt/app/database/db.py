from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from torgpt.app.database.models.user import User
from torgpt.app.config import Settings
from bcrypt import bcrypt
settings = Settings()

SQLALCHEMY_DATABASE_URL = settings.database_url
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_user_by_username(username: str):
    with SessionLocal() as session:
        return session.query(User).filter(User.username == username).first()

def create_user(username: str, password: str):
    hashed_password = bcrypt.hash(password)
    user = User(username=username, hashed_password=hashed_password)
    with SessionLocal() as session:
        session.add(user)
        session.commit()
