import utils, math

from flask import render_template, request
from app import app

@app.route('/products')
def products():
    category_id = request.args.get('category_id')
    products = utils.load_products(category_id)
    return render_template("products.html", products=products)

@app.route('/products/<int:product_id>')
def product(product_id):
    product = list(utils.load_products_by_id(product_id))[0]
    return render_template("product_detail.html", product=product)

@app.route("/")
def index():

    category_id = request.args.get('category_id')
    page = int(request.args.get('page', 1))

    categories = utils.load_categories()
    products = utils.load_products(category_id=category_id, page=page)
    total_product = utils.count_product(products)

    return render_template("index.html",
                           categories=categories,
                           products=products,
                           pages=math.ceil(total_product / app.config['PAGE_SIZE']))

if __name__ == "__main__":
    from app.admin import *
    app.run(debug=True)
