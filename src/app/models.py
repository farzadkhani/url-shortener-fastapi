from .database import Base, engine
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class UserModel(Base):
    """
    class for create user table
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
    hashed_password = Column(String)


class ShortenerURLModel(Base):
    """
    Shorterner URL Model
    """

    __tablename__ = "redirect"

    id = Column(Integer, primary_key=True)
    short_url = Column(String(255), nullable=False, unique=True)
    url = Column(Text, nullable=False)
    visit_counter = Column(Integer, default=0)


Base.metadata.create_all(engine)  # Create tables
