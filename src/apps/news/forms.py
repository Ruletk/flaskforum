from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField


class CreateNewsForm(FlaskForm):
    title = StringField(max_length=100, label=_l("News title"))
    content = TextAreaField(label=_l("News content"))
