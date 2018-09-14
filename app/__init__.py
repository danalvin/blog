from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from .forms import RegistrationForm, LoginForm 



app = Flask(__name__)
app.config['SECRET_KEY'] = '1q2w3e4r'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import views