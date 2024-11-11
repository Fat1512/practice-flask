import json


def load_json(path):
    with open(path, "r") as f:
        return json.load(f)


def count_cart(cart):
    total_amount, total_item = 0, 0
    for c in cart.values():
        total_amount += c['price']
        total_item += c['quantity']
    return {
        'total_amount': total_amount,
        'total_item': total_item
    }






































