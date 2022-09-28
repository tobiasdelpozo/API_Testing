import datetime
import uuid
from marshmallow import Schema, fields, post_load


class Order:
    def __init__(self, price: float, quantity: int, side: int) -> None:
        if (price <= 0) or (quantity <= 0):
            raise ValueError("Negative/0 price!")
        if abs(side) != 1:
            raise ValueError("No side!")

        self.__price = price
        self.__quantity = quantity
        self.__id = uuid.uuid4()
        self.__time_created = datetime.datetime.now()
        self.__time_updated = self.__time_created
        self.__side = side

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, p: float):
        if p <= 0:
            raise ValueError("Negative/0 price!")
        self.__price = p
        self.__time_updated = datetime.datetime.now()

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, q: int):
        if q <= 0:
            raise ValueError("Negative/0 quantity!")
        self.__quantity = q
        self.__time_updated = datetime.datetime.now()

    @property
    def time_created(self) -> datetime.datetime:
        return self.__time_created

    @property
    def time_updated(self) -> datetime.datetime:
        return self.__time_updated

    @property
    def id(self) -> str:
        return self.__id

    @property
    def side(self) -> int:
        return self.__side

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}:
    -ID: {self.__id}
    -Price: {self.__price}
    -Qty: {self.__quantity}
    -Created: {self.__time_created.strftime('%Y-%m-%d %H:%M:%S')}
    -Updated: {self.__time_updated.strftime('%Y-%m-%d %H:%M:%S')}
    -Side: {'SELL' if self.__side == -1 else 'BUY'}"""


class OrderSchema(Schema):
    price = fields.Float()
    quantity = fields.Integer()
    id = fields.UUID()
    time_created = fields.DateTime()
    time_updated = fields.DateTime()
    side = fields.Integer()

    @post_load
    def make_order(self, data, **kwargs) -> Order:
        return Order(**data)
