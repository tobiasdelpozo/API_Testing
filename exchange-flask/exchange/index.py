import json
from flask import Flask, jsonify, request
from model.order_book import Order, OrderSchema

app = Flask(__name__)

book = [Order(10.1, 4, -1), Order(1100.2, 400, 1)]


@app.route("/orders", methods=["GET"])
def get_orders():
    schema = OrderSchema(many=True)
    return jsonify(schema.dump(book))


@app.route("/orders", methods=["POST"])
def add_order():
    order = OrderSchema().load(request.get_json())
    book.append(order)
    return "", 204
