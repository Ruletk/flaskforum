from flask_login import current_user


def inject_user():
    return {"user": current_user}


def init_context_processors(app):
    app.context_processor(inject_user)
