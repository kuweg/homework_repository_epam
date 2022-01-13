from homework11.hw2 import (Order, bad_discount, evening_discount,
                            morning_discount)


def test_morning_discount():
    """Testing that morning discount calculated correctly."""
    order = Order(100, morning_discount)
    assert order.final_price() == 75.


def test_evening_discount():
    """Testing that evening discount calculated correctly."""
    order = Order(100, evening_discount)
    assert order.final_price() == 25.


def test_bad_discount():
    """Testing, that unfair discount rate won't be used."""
    order = Order(100, bad_discount)
    assert order.final_price() == order.price


def test_bad_pricing_strategy():
    """Testing, that suspicious pricing policy will be fixed."""
    order = Order(-100, morning_discount)
    assert order.price == 100
