from functools import wraps

from flask import abort
from flask import redirect
from flask import url_for
from flask_login import current_user


MAIN_PAGE = "index"


def staff_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_staff or current_user.is_superuser:
            return func(*args, **kwargs)
        abort(403)

    return wrapper


def superuser_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_superuser:
            return func(*args, **kwargs)
        abort(403)

    return wrapper


def anonymous_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for(MAIN_PAGE))
        return func(*args, **kwargs)

    return wrapper


def login_redirect_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_anonymous:
            return redirect(url_for(MAIN_PAGE))
        return func(*args, **kwargs)

    return wrapper
