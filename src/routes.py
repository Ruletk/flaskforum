from flask import render_template
from flask import send_from_directory

from src.apps.news import news_bp
from src.apps.users import user_bp
from src.extensions import login
from src.models import User


def route(app):
    # Registering blueprints ...
    app.register_blueprint(user_bp)
    app.register_blueprint(news_bp)

    # Registering routes ...

    other_routes(app)
    error_routes(app)


def error_routes(app):
    @app.errorhandler(404)
    def error_404(error):
        return render_template("errors/404.html")

    @app.errorhandler(401)
    def error(error):
        return render_template("errors/401.html")


def other_routes(app):
    @app.route("/")
    def index():
        return render_template("main/index.html")

    @app.route("/media/<path:filename>")
    def media(filename=""):
        return send_from_directory(app.config["MEDIA_FOLDER"], filename)

    @login.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
