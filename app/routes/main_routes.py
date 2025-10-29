from flask import Blueprint, render_template, redirect, url_for, flash, session, request
import time
import os
from utils import db
import random

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("home.html")

@main_bp.route("/about")
def about():
    return render_template("about.html")