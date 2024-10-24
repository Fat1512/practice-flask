from app import app, db
from app.model import Category, Product
from sqlalchemy import or_
import json, os

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

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

def count_product(products):
    return Product.query.filter(Product.active.__eq__(True)).filter(Product.id in products.id).count()