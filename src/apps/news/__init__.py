from flask import Blueprint


news_bp = Blueprint("news", __name__)

from src.apps.news import models  # noqa: F401
from src.apps.news import routes  # noqa: F401
