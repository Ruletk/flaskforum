import os
from pathlib import Path

from dotenv import load_dotenv

APP_ROOT = Path(__file__).parent.parent.parent
APP_FOLDER = Path(__file__).parent
load_dotenv(os.path.join(APP_ROOT, ".env"))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG = True
    MEDIA_FOLDER = os.path.join(APP_ROOT, "media")
    AVATAR_FILETYPES = (".png", ".jpg", ".jpeg", ".gif")
    LANGUAGES = ["en", "ru"]
