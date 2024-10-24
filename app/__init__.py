from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = '!@#!%!@#!@QDAFSDadd214FESF!#!@#@!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:15122004@localhost:3306/labsaledb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 4
db=SQLAlchemy(app=app)