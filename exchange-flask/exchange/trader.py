import requests
from model.order_book import Order, OrderSchema
from time import sleep
import json

if __name__ == "__main__":
    url = "http://0.0.0.0:3000/orders"
    for i in range(10):
        data = Order(10.2 + i, i + 1, -1)
        schema = OrderSchema()
        order = schema.dump(data)
        order = {
            "price": order["price"],
            "quantity": order["quantity"],
            "side": order["side"],
        }
        requests.post(url=url, json=json.dumps(order))
        print(requests.get(url=url).json())
        sleep(1)
