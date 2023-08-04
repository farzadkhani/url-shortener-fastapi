from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    """
    User Base Schema
    """

    email: str
    first_name: str
    last_name: str


class UserCreateSchema(UserBaseSchema):
    """
    User Create Schema
    """

    password: str


class UserSchema(UserCreateSchema):
    """
    User Schema
    """

    id: int
    is_active: bool

    class Config:
        orm_mode = True


class ShortenerURLBaseSchema(BaseModel):
    """
    Shortener URL Schema
    """

    short_url: str
    url: str


class ShortenerURLCreateSchema(ShortenerURLBaseSchema):
    """
    Shortener URL Create Schema
    """

    pass


class ShortenerURLSchema(ShortenerURLCreateSchema):
    """
    Shortener URL Schema
    """

    id: int
    visit_counter: int

    class Config:
        orm_mode = True
