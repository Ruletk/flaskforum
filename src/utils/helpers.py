from flask import current_app
from flask import request
from PIL import Image


IMG_SIZE = (512, 512)


def get_locale():
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])


def resize_image(file, f_type):
    if f_type != "gif":
        image = Image.open(file)
        return image.resize(IMG_SIZE, Image.Resampling.LANCZOS)


def set_filetype(filename: str) -> str:
    return "png" if filename.rsplit(".", 1)[-1] != "gif" else "gif"
