from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db, app
from datetime import datetime
import utils

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(Integer, primary_key=True, autoincrement=True)

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
        # db.create_all()
        # c1 = Category(name='Dien thoai')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='Tai nghe')
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        products = utils.load_products()
        for p in products:
            product = Product(name=p['name'],
                              description=p['description'],
                              price=p['price'],
                              image=p['image'],
                              category_id=p['category_id'])
            db.session.add(product)

        db.session.commit()