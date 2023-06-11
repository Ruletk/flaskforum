from flask import current_app
from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from wtforms import (
    StringField,
    EmailField,
    PasswordField,
    SubmitField,
    BooleanField,
    FileField,
)
from wtforms.validators import DataRequired, Length, EqualTo, Email

from app.src.models import User


class SignUpForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired(), Length(max=50)])
    email = EmailField(
        _l("E-mail"), validators=[DataRequired(), Length(max=100), Email()]
    )
    password1 = PasswordField(
        _l("Password"), validators=[DataRequired(), Length(min=8)]
    )
    password2 = PasswordField(_l("Repeat password"), validators=[EqualTo("password1")])
    submit = SubmitField(_l("SignUp"))


class SignInForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    remember_me = BooleanField(_l("Remember me"))
    submit = SubmitField(_l("SignIn"))


class AvatarForm(FlaskForm):
    image = FileField(_l("Avatar"), validators=[DataRequired()])
    submit = SubmitField(_l("Change"))

    def validate_on_submit(self, extra_validators=None):
        if self.image.data and not self.image.data.filename.endswith(
            current_app.config["AVATAR_FILETYPES"]
        ):
            return False
        return super().validate_on_submit(extra_validators)
