from PIL import Image
from flask import request, current_app


IMG_SIZE = (512, 512)


def get_locale():
    return request.accept_languages.best_match(current_app.config["LANGUAGES"])


def resize_image(file):
    image = Image.open(file)
    return image.resize(IMG_SIZE, Image.Resampling.LANCZOS)
