from flask import Blueprint, render_template, redirect, url_for, flash, session, request
import time
import os
from utils import db
import random

product_bp = Blueprint('product_bp', __name__)

@product_bp.route("/products")
def products():
    return render_template("product.html")
