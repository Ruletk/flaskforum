from pathlib import Path

from flask import current_app
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from . import Base
from src.extensions import db
from src.utils.helpers import resize_image
from src.utils.helpers import set_filetype


class User(Base, UserMixin):
    __tablename__ = "users"

    json_attributes = ("username", "email")

    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(70), unique=True, nullable=False, index=True)
    _password_hash = db.Column(db.String(128))

    avatar = db.Column(db.String(255), default="/users/avatars/noavatar.png")

    def save(self, password=None):
        if password:
            self.set_password(password)
        return super().save()

    def check_password(self, password):
        return check_password_hash(self._password_hash, password)

    def set_password(self, password):
        self._password_hash = generate_password_hash(password)

    def __str__(self):
        return "<User %s>" % self.username

    def __repr__(self):
        return "<User %s>" % self.username

    def set_avatar(self, file):
        f_type = set_filetype(file.filename)
        path = f"users/avatars/{self.username}.{f_type}"
        image = resize_image(file, f_type)
        image.save(Path(current_app.config["MEDIA_FOLDER"]) / path, format=f_type)
        self.update(avatar=path)
