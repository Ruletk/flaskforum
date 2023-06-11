from .utils.helpers import get_locale
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_babel import Babel


db = SQLAlchemy()
migrage = Migrate()
login = LoginManager()
babel = Babel()


def init_apps(app):
    db.init_app(app)
    login.init_app(app)
    babel.init_app(app, locale_selector=get_locale)
    migrage.init_app(app, db)
