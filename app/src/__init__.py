from flask import Flask

from .config import Config
from .extensions import init_apps, babel
from .routes import route
from .utils.context_processors import init_context_processors


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_apps(app)
    init_context_processors(app)
    route(app)

    from . import models

    return app
