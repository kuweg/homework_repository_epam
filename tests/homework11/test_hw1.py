from enum import Enum

from homework11.hw1 import SimplifiedEnum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class ColorsSimplifiedEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class ColorsEnumMixed(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE")
    ORANGE = "ORANGE"
    BLACK = "BLACK"


def test_compare_attributes():
    """Testing that attributes were set correctly."""
    assert ColorsEnum.RED.value == ColorsSimplifiedEnum.RED == "RED"


def test_keys_attrs_from_mixed_class():
    """Testing that __keys attributes were set in mixed class."""
    assert ColorsEnumMixed.RED == "RED"


def test_attr_from_mixed_class():
    """Testing that metaclass does not change standard behaviour."""
    assert ColorsEnumMixed.BLACK == "BLACK"
