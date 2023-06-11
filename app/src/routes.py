from flask import send_from_directory, render_template

from .apps.users import user_bp
from .extensions import login
from .models import User


def route(app):
    # Registering blueprints ...
    app.register_blueprint(user_bp)

    # Registering routes ...
    @app.route("/")
    def index():
        return "<h1>Index</h1>"

    @app.route("/media/<path:filename>")
    def media(filename=""):
        dir = app.config["MEDIA_FOLDER"]
        return send_from_directory(dir, filename)

    @login.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    error_routes(app)


def error_routes(app):
    @app.errorhandler(404)
    def error_404(error):
        return render_template("errors/404.html")

    @app.errorhandler(401)
    def error(error):
        return render_template("errors/401.html")
