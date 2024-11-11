import utils, math
from flask import render_template, request, redirect, url_for, session, jsonify
from app import app, login
from flask_login import login_user, logout_user
import cv2
from pyzbar.pyzbar import decode
import asyncio

@app.context_processor
def common_response():
    return {
        'categories': utils.load_categories()
    }

#get called whenever login successfully
@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)

@app.route('/products')
def products():
    category_id = request.args.get('category_id')
    products = utils.load_products(category_id)
    return render_template("products.html", products=products)


@app.route('/products/<int:product_id>')
def product(product_id):
    product = list(utils.load_products_by_id(product_id))[0]
    return render_template("product_detail.html", product=product)


@app.route("/user/register", methods=["GET", "POST"])
def register():
    if request.method.__eq__("GET"):
        return render_template("register.html")
    name = request.form.get("name")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    repeat_password = request.form.get("repeat_password")

    err_msg = ''
    try:
        if password.strip().__eq__(repeat_password.strip()):
            avatar = request.form.get('avatar')
            avatar_url = ''
            # if avatar:
            # res = cloudinary.uploader.upload(avatar)
            # avatar_url = res['secure_url']
            utils.add_user(name=name,
                           username=username,
                           email=email,
                           password=password,
                           repeat_password=repeat_password,
                           avatar=avatar_url)
            return redirect(url_for('index'))
        else:
            err_msg = "Sai mat khau"
    except Exception as e:
        err_msg = 'He thong co loi: ' + str(e)

    return render_template('register.html', err_msg=err_msg)


@app.route("/user/login", methods=["get", "post"])
def login():
    err_msg = ''
    if request.method.__eq__("POST"):
        username = request.form['username']
        password = request.form['password']
        user = utils.check_login(username, password)

        if user:
            login_user(user)
            return redirect(url_for("index"))
        else:
            err_msg = "Sai mat khau"
        return render_template("index.html")
    return render_template("login.html", err_msg=err_msg)

@app.route("/user/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/")
def index():
    category_id = request.args.get('category_id')
    page = int(request.args.get('page', 1))

    products = utils.load_products(category_id=category_id, page=page)
    total_product = utils.count_product()

    return render_template("index.html",
                           products=products,
                           pages=math.ceil(total_product / app.config['PAGE_SIZE']))

@app.route("/api/barcode")
def barcode():

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    camera = True
    print("day ne")

    while camera == True:
        success, frame = cap.read()
        x = cv2.waitKey(50)
        print(x)
        if x == 113:
            for code in decode(frame):
                print(code.type)
                print(code.data.decode('utf-8'))
        elif x == 27:
            print("falsy valye")
            break
        cv2.imshow('Testing-code-scan', frame)
    cap.release()
    cv2.destroyAllWindows()
    return "12"


@app.route("/api/cart", methods=['post'])
def cart():

    data = request.json
    id = str(data.get("id"))
    name = data.get("name")
    price = data.get("price")

    cart = session.get('cart')
    if not cart:
        cart = {}
    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            'id': id,
            'name': name,
            'price': price,
            'quantity': 1
        }
    session['cart'] = cart
    return jsonify(utils.count_cart(cart))

if __name__ == "__main__":
    from app.admin import *

    app.run(debug=True)
