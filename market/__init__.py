from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# create the app
app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = 'f9472fafa5e0e075e665ff67'
csrf = CSRFProtect(app)


db = SQLAlchemy()
db.init_app(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = 'login'
loginManager.login_message_category = 'info'

from market import routes


