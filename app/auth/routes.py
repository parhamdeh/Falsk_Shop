from flask import Blueprint, render_template, redirect, url_for, flash, session, request
import time
import os
from app.auth.forms import LoginForm, SignUpForm, UploadProfilePictureForm
from utils import db
import random

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

    # تولید کپچا هنگام GET
    if request.method == "GET":
        a, b = random.randint(1, 9), random.randint(1, 9)
        session["captcha_answer"] = str(a + b)
        session["captcha_question"] = f"{a} + {b} = ؟"

    if form.validate_on_submit():
        user_captcha = form.captcha.data.strip()
        expected = session.get("captcha_answer")

        if user_captcha != expected:
            flash("کپچا اشتباه است!", "danger")
            return redirect(url_for("auth.signup"))

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
            flash("شما قبلا با این ایمیل اکانت ساخته‌اید!", "danger")
        else:
            flash("خطای ناشناخته", "danger")

    return render_template("signup.html", form=form, captcha_question=session.get("captcha_question"))

@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("شما با موفقیت خارج شدید!", "success")
    return redirect(url_for("auth.start"))

@auth_bp.route("/dashboard")
def dashboard():
    if "username" in session and session["logged_in"]:
        return render_template("dashboard.html", username=session["username"])
    else:
        flash("لطفاً ابتدا وارد شوید!", "danger")
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

UPLOAD_FOLDER = 'app/static/profile_pics'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@auth_bp.route("/upload_profile_picture", methods=["GET", "POST"])
def upload_profile_picture():
    if not session.get("logged_in"):
        return redirect(url_for("auth.login"))
    
    form = UploadProfilePictureForm()
    if form.validate_on_submit():
        file = form.profile_picture.data
        if file and allowed_file(file.filename):
            filename = f"{session['username']}_profile.png"
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            session['profile_picture'] = filename
            flash("عکس پروفایل با موفقیت آپلود شد!", "success")
            return redirect(url_for("auth.dashboard"))
        else:
            flash("فرمت فایل نامعتبر است!", "danger")
    return render_template("upload_profile_picture.html", form=form)