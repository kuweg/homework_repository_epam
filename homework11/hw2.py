"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75

order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from typing import Callable

from .utils.discount_validator import DiscountValidator
from .utils.order import OrderObj
from .utils.price_validator import PriceValidator


class Order(OrderObj):

    discount_strategy = DiscountValidator()
    price = PriceValidator()

    def __init__(self, price: float,
                 discount_strategy: Callable = None) -> None:
        """
        :param price: price for order
        :type price: float
        :param discount_strategy: a discount type
        :type discount_strategy: Callable object
        """
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        """
        Applies passed discount to current price.

        :return: final price after discount
        :rtype: float
        """
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0

        return self.price - discount

    def __repr__(self) -> str:
        return (
            f"<Order price is {self.price} with "
            + f"{getattr(self.discount_strategy,'__name__', None)} strategy>"
        )


def morning_discount(order: Order):
    return order.price * 0.25


def evening_discount(order: Order):
    return order.price * 0.75


def bad_discount(order: Order):
    return 100000
