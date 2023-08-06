from flask import current_app
from flask import flash
from flask_babel import gettext as _
from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import EmailField
from wtforms import FileField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length


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

    def validate_on_submit(self, extra_validators=None):
        if self.password1.data != self.password2.data:
            flash(_("Passwords doesn't match"))
            return False
        return super().validate_on_submit(extra_validators)


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


class DeleteAccountForm(FlaskForm):
    submit = SubmitField(_l("Are you sure?"))

    class Meta:
        csrf = False
