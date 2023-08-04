from sqlalchemy.orm import Session

from . import models, schemas
from .utils import hashing_password


def get_user(db: Session, user_id: int):
    return db.query(models.UserModel).filter(models.UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.UserModel).filter(models.UserModel.email == email).first()


def get_user_by_firt_name(db: Session, first_name: str):
    return (
        db.query(models.UserModel)
        .filter(models.UserModel.first_name == first_name)
        .first()
    )


def get_user_by_last_name(db: Session, last_name: str):
    return (
        db.query(models.UserModel)
        .filter(models.UserModel.last_name == last_name)
        .first()
    )


def get_active_users(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.UserModel)
        .filter(models.UserModel.is_active == True)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_user(db: Session, user: schemas.UserCreateSchema):
    fake_hashed_password = hashing_password(user.password)
    db_user = models.UserModel(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=fake_hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_shortener_url(db: Session, shortener_url_id: int):
    return (
        db.query(models.ShortenerURLModel)
        .filter(models.ShortenerURLModel.id == shortener_url_id)
        .first()
    )


def create_shortener_url(db: Session, shortener_url: schemas.ShortenerURLCreateSchema):
    db_shortener_url = models.ShortenerURLModel(
        short_url=shortener_url.short_url, url=shortener_url.url
    )
    db.add(db_shortener_url)
    db.commit()
    db.refresh(db_shortener_url)
    return db_shortener_url
