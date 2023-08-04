from sqladmin import Admin, ModelView
from .models import UserModel, ShortenerURLModel

from app import app, engine

admin = Admin(app, engine)


class UserModelAdmin(ModelView, model=UserModel):
    columen_list = ["id", "name"]


admin.add_view(UserModelAdmin)


class ShortenerURLModelAdmin(ModelView, model=ShortenerURLModel):
    columen_list = [
        "id",
        "short_url",
        "url",
        "visit_counter",
    ]


admin.add_view(ShortenerURLModelAdmin)
