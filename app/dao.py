from app import app, db
from app.model import Category, Product, User
from sqlalchemy import or_
import json, os
import hashlib

from app.utils import load_json


def load_categories():
    return Category.query.all()
    # return load_json(os.path.join(app.root_path + "/data/categories.json"))

def load_products(category_id=None, page=1):
    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size
    end = start + page_size
    return (Product.query.filter(Product.active.__eq__(True))
            .filter(or_(category_id is None, Product.category_id.__eq__(category_id)))
            .slice(start, end).all())
    # products = load_json(os.path.join(app.root_path + "/data/products.json"))
    # return filter(lambda prod: category_id is None or prod["category_id"] == int(category_id), products)

def load_products_by_id(product_id):
    Product.query.get(product_id)
    # products = load_json(os.path.join(app.root_path + "/data/products.json"))
    # return filter(lambda prod: prod["id"] == product_id, products)

def load_file_product_to_db():
    products = load_json(os.path.join(app.root_path + "/data/products.json"))
    for p in products:
        product = Product(name=p['name'],
                          description=p['description'],
                          price=p['price'],
                          image=p['image'],
                          category_id=p['category_id'])
        db.session.add(product)
    db.session.commit()

def add_user(name, username, password, **kwargs):
    password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
    user = User(name=name.strip(),
                username=username.strip(),
                password=password,
                avatar=kwargs.get("avatar"),
                email=kwargs.get("email"))
    db.session.add(user)
    db.session.commit()

def check_login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password.strip())).first()

def get_user_by_id(user_id):
    return User.query.get(int(user_id))

def count_product():
    return Product.query.filter(Product.active.__eq__(True)).count()

