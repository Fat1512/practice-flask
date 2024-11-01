from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from urllib.parse import quote
import cloudinary

app = Flask(__name__)
app.secret_key = '!@#!%!@#!@QDAFSDadd214FESF!#!@#@!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost:3306/labsaledb?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 6

db=SQLAlchemy(app=app)

cloudinary.config(
  cloud_name = "dq27ted4k",
  api_key = "454888958582644",
  api_secret = "v3nSeB0oLKHwrU2Un7T5b4R5If0",
  secure = True
)

login = LoginManager(app=app)
login.login_view='login'