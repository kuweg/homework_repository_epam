from __future__ import annotations

from typing import Callable

from .order import OrderObj


class PriceValidator:
    """
    Descriptor class for 'price' value validation.
    Multiply price by (-1) if it is negative.
    Example: -100 => 100
    :return: passed price
    :rtype: int or float
    """

    @staticmethod
    def _validation(value) -> bool:
        """
        Checking value beging negative and returnig bool.
        :param value: pased price to Order class
        :type value: int or float
        :return: True if price positive else False
        :rtype: False
        """
        try:
            if value < 0:
                raise ValueError
        except ValueError:
            return False
        return True

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance: OrderObj, value: Callable = None) -> None:
        if self._validation(value):
            setattr(instance, self._name, value)
        else:
            setattr(instance, self._name, -1 * value)

    def __set_name__(self, instance, name):
        self._name = f"_{name}"
