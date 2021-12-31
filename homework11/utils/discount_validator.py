from __future__ import annotations

from typing import Callable

from .order import OrderObj


class DiscountValidator:
    """
    Descriptor class for discount validation.
    Checks that discount is not greater than price otherwise nullifies it.

    :return: discount if its valid or None
    :rtype: float/ int/ None
    """
    @staticmethod
    def _validation(instance: OrderObj, value: Callable) -> bool:

        try:
            if instance.price - value(instance) < 0:
                raise ValueError
        except ValueError:
            return False
        return True

    def __get__(self, instance, owner):
        return getattr(instance, self._name)

    def __set__(self, instance: OrderObj, value: Callable = None) -> None:

        if value and self._validation(instance, value):
            setattr(instance, self._name, value)
        else:
            setattr(instance, self._name, None)

    def __set_name__(self, instance, name):
        self._name = f"_{name}"
