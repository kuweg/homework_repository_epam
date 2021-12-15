import os

from homework8.task2 import TableData

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
datatable_path = os.path.join(BASE_DIR, "example.sqlite")
presidents = TableData(datatable_path, "presidents")
presidents2 = TableData(datatable_path, "presidents")


def test_len():
    assert len(presidents) == 3


def test_getitem():
    assert presidents["Trump"] == ("Trump", 1337, "US")


def test_contains():
    assert "Yeltsin" in presidents


def test_contains_negative():
    assert "Medvedev" not in presidents


def test_iteration(capsys):
    for president in presidents:
        print(president["name"])
    captured = capsys.readouterr()
    assert captured.out == "Yeltsin\nTrump\nBig Man Tyrone\n"


def test_singleton_connection():
    assert id(presidents.cursor) == id(presidents2.cursor)
