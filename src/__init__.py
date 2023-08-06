from flask import Flask

from src.config import Config
from src.extensions import init_apps
from src.routes import route
from src.utils.context_processors import init_context_processors


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_apps(app)
    init_context_processors(app)
    route(app)

    from src import models  # noqa: F401

    return app
