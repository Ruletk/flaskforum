from flask import Blueprint


user_bp = Blueprint("users", __name__)

from src.apps.users import routes  # noqa: F401
