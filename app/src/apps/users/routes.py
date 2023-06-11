from flask import request, render_template, flash, redirect, url_for, jsonify, session
from flask_login import login_user, login_required, current_user
from flask_babel import gettext as _

from app.src.models import User
from app.src.utils.decorators.routes import anonymous_only
from . import user_bp
from .forms import SignUpForm, SignInForm, AvatarForm


@user_bp.route("/registration", methods=["GET", "POST"])
@user_bp.route("/signup", methods=["GET", "POST"])
@anonymous_only
def signup():
    form = SignUpForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data).first():
                print("Flash")
                flash(_("A user with the same username already exists."))
            elif User.query.filter_by(email=form.email.data).first():
                print("Flash")
                flash(_("A user with the same email already exists."))
            else:
                user = User(username=form.username.data, email=form.email.data)
                user.save(password=form.password1.data)
                login_user(user)
                session.permanent = True
                return redirect(url_for("users.profile"))
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
