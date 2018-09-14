from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .forms import RegistrationForm, LoginForm 
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '1q2w3e4r'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
loginmanager = LoginManager(app) 
loginmanager.login_view = 'login'
loginmanager.login_message_category = 'info'

from app import views