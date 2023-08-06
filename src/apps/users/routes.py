from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_babel import gettext as _
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from src.apps.users import user_bp
from src.apps.users.forms import AvatarForm
from src.apps.users.forms import DeleteAccountForm
from src.apps.users.forms import SignInForm
from src.apps.users.forms import SignUpForm
from src.models import User
from src.utils.decorators.routes import anonymous_only


@user_bp.route("/registration", methods=["GET", "POST"])
@user_bp.route("/signup", methods=["GET", "POST"])
@anonymous_only
def signup():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data).first():
                flash(_("A user with the same username already exists."))
            elif User.query.filter_by(email=form.email.data).first():
                flash(_("A user with the same email already exists."))
            else:
                user = User(username=form.username.data, email=form.email.data)
                user.save(password=form.password1.data)
                login_user(user)
                session.permanent = True
                return redirect(url_for("users.profile", username=user.username))
    return render_template("users/signup.html", form=form)


@user_bp.route("/login", methods=["GET", "POST"])
@user_bp.route("/signin", methods=["GET", "POST"])
@anonymous_only
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            if form.remember_me:
                session.permanent = True
            return redirect(url_for("index"))
        flash(_("Wrong username or password"))

    return render_template("users/signin.html", form=form)


@user_bp.route("/logout")
@user_bp.route("/signout")
def signout():
    if current_user.is_authenticated:
        flash(_("You are logged out"))
    logout_user()
    return redirect(url_for("index"))


@user_bp.route("/profile/<username>")
def profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template("users/profile.html", us=user)


@user_bp.route("/change_avatar", methods=["GET", "POST"])
def change_avatar():
    form = AvatarForm()
    if request.method == "POST":
        if form.validate_on_submit() and request.files.get("image", None):
            current_user.set_avatar(request.files.get("image"))
            return redirect(url_for("users.profile", username=current_user.username))
    return render_template("users/change_avatar.html", form=form)


@user_bp.route("/delete_account", methods=["GET", "POST"])
@login_required
def delete_account():
    form = DeleteAccountForm()
    if request.method == "POST" and form.validate_on_submit():
        current_user.delete()
        return redirect(url_for("index"))
    flash(_("Your account has been deleted"))
    return render_template("users/account_delete.html", form=form)
