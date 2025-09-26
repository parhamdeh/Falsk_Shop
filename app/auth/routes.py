from flask import Blueprint, render_template, redirect, url_for, flash, session
import time
from app.auth.forms import LoginForm, SignUpForm
from utils import db

# تغییر مهم: اضافه کردن url_prefix
auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/")
def start():
    return render_template("index.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():        
        username = form.username.data
        password = form.password.data

        result = db.mongo.check_login(username, password)
        if result == 1:
            session["username"] = username
            session["logged_in"] = True
            flash(f"خوش آمدی {username}!", "success")
            time.sleep(3)
            return redirect(url_for("auth.dashboard"))
        elif result == "passwordError":
            flash("رمز اشتباه است!", "danger")
        elif result == "usernameError":
            flash("نام کاربری اشتباه است!", "danger")
        else:
            flash("خطای ناشناخته!", "danger")
    return render_template("login.html", form=form)

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        result = db.mongo.Add_User(username=username, email=email, password=password)
        
        if result == 1:
            flash("ثبت‌نام موفقیت‌آمیز بود!", "success")
            time.sleep(3)
            return redirect(url_for("auth.login"))
        elif result == 2:
            flash("این نام کاربری قبلاً وجود دارد!", "danger")
        elif result == 3:
            flash("شما قبلا با این ایمیل اکانت ساخته اید!", "danger")
        else:
            flash("خطای ناشناخته", "danger")

    return render_template("signup.html", form=form)

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("شما با موفقیت خارج شدید!", "success")
    return redirect(url_for("auth.start"))

@auth_bp.route("/dashboard")
def dashboard():
    if "username" in session and session["logged_in"]:
        return render_template("dashboard.html")
    else:
        flash("لطفا ابتدا وارد شوید!", "danger")
        return redirect(url_for("auth.login"))

@auth_bp.route("/cart")
def cart():
    if session.get("logged_in"):
        return "صفحه سبد خرید - به زودی"
    return redirect(url_for("auth.login"))

@auth_bp.route("/change_credentials")
def change_credentials():
    if session.get("logged_in"):
        return "صفحه تغییر اطلاعات - به زودی"
    return redirect(url_for("auth.login"))

@auth_bp.route("/delete_account")
def delete_account():
    if session.get("logged_in"):
        return "صفحه حذف حساب - به زودی"
    return redirect(url_for("auth.login"))

@auth_bp.route("/charge")
def charge():
    if session.get("logged_in"):
        return "صفحه شارژ حساب - به زودی"
    return redirect(url_for("auth.login"))