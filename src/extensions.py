from flask_babel import Babel
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from src.utils.helpers import get_locale


db = SQLAlchemy()
migrage = Migrate()
login = LoginManager()
babel = Babel()


def init_apps(app):
    db.init_app(app)
    login.init_app(app)
    babel.init_app(app, locale_selector=get_locale)
    migrage.init_app(app, db)
