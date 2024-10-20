from sqlalchemy import Column, Integer, String
from torgpt.app.database.db import Base
from passlib.hash import bcrypt

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    def verify_password(self, password: str) -> bool:
        return bcrypt.verify(password, self.hashed_password)
