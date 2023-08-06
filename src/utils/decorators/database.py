from functools import wraps

from src.extensions import db


def clear_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as ex:
            db.session.remove()
            raise ex

    return wrapper


def rollback_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as ex:
            db.session.rollback()
            raise ex

    return wrapper
