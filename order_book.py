import time
import datetime
import uuid
from enum import Enum, unique


@unique
class Side(Enum):
    BUY = 1
    SELL = -1


class BaseOrder:
    def __init__(self, price: float, quantity: int) -> None:
        if (price <= 0) or (quantity <= 0):
            raise ValueError("Negative/0 price!")
        self.__price = price
        self.__quantity = quantity
        self.__id = uuid.uuid4()
        self.__time_created = datetime.datetime.now()
        self.__time_updated = self.__time_created

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
    def get_id(self) -> uuid.UUID:
        return self.__id

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}:
    -ID: {self.__id}
    -Price: {self.__price}
    -Qty: {self.quantity}
    -Created: {self.__time_created.strftime('%Y-%m-%d %H:%M:%S')}
    -Updated: {self.__time_updated.strftime('%Y-%m-%d %H:%M:%S')}"""


class BuyOrder(BaseOrder):
    def __init__(self, price: float, quantity: int) -> None:
        super().__init__(price, quantity)
        self.__side = Side.BUY

    @property
    def side(self):
        return self.__side

    def __repr__(self) -> str:
        return super().__repr__() + f"\n    -Side: {self.__side.name}"


class SellOrder(BaseOrder):
    def __init__(self, price: float, quantity: int) -> None:
        super().__init__(price, quantity)
        self.__side = Side.SELL

    @property
    def side(self):
        return self.__side

    def __repr__(self) -> str:
        return super().__repr__() + f"\n    -Side: {self.__side.name}"


print(SellOrder(1, 2))
