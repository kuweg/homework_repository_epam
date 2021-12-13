import os

from homework8.task1 import KeyValueStorage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
test_file_path = os.path.join(BASE_DIR, "task1.txt")
storage = KeyValueStorage(test_file_path)


def test_name_attr():
    assert storage.name == "kek"


def test_song_attr():
    assert storage.song == "shadilay"


def test_power_attr():
    assert storage.power == 9001


def test_power_attr_type():
    assert isinstance(storage.power, int)
