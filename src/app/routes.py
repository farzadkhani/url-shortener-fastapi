from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session

from . import app, database, cruds, models, schemas


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    # base route of project
    return {"Hello": "World"}


@app.post("/users/", response_model=schemas.UserSchema)
def create_user(user: schemas.UserCreateSchema, db: Session = Depends(get_db)):
    db_user = cruds.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )
    user_object = cruds.create_user(db=db, user=user)
    return {"data": user_object}
