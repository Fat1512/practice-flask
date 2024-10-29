from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app import db, app
from enum import Enum as EnumRole
from datetime import datetime
from flask_login import UserMixin

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(Integer, primary_key=True, autoincrement=True)

class Role(EnumRole):
    ADMIN = 1
    CUSTOMER = 2

class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    avatar = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    user_role = Column(Enum(Role), default=Role.CUSTOMER)

    def __str__(self):
        return self.name
    def get_id(self):
        return str(self.id)


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=False)

    def __str__(self):
        return self.name

class Product(BaseModel):
    __tablename__ = 'product'
    name = Column(String(50))
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable = False)

    def __str__(self):
        return self.name



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()
        # c1 = Category(name='Dien thoai')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Tai nghe')
        #
        # db.session.add(c1)s
        # db.session.add(c2)
        # db.session.add(c3)
        # products = utils.load_products()
        # for p in products:
        #     product = Product(name=p['name'],
        #                       description=p['description'],
        #                       price=p['price'],
        #                       image=p['image'],
        #                       category_id=p['category_id'])
        #     db.session.add(product)
        #
        # db.session.commit()