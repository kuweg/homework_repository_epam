import os
from typing import Generator


class KeyValueStorage:
    """Wrapper class which works with key/value storage files.
    Storage format:

    key1=value1
    key2=value2
    ...etc

    Keys become an attributes with corresponding values.
    """

    def _split_and_check_key(self, line: str, split_sign: str):
        """Splits line by given sign and checks key.

        :param line: input string line
        :param split_char: character for split
        :return: returns checked key and corresponding value
        """

        key, value = line.split(split_sign)
        if not key.isidentifier():
            raise ValueError("Cannot be used as variable name!")
        return key, value

    def _open_file(self, file_path: str, access_mode: str) -> Generator:
        """Reads file line by line and acting like generator object.
           Returns FileExistsError otherwise.

        :pararm file_path: path to file
        :type file_path: str
        :param access_mode: mode for built-in function open()
        :type access_mode: str
        :return: line by line iterator
        """
        if os.path.isfile(file_path):
            with open(file_path, access_mode) as file_handler:
                for line in file_handler.readlines():
                    yield line
        else:
            raise FileExistsError("File does not exist")

    def __init__(self, path_to_file: str) -> None:
        """Constructing an inner dict with key/value from file.
        :param path_to_file: path to key/value storage file
        """
        self.items = {}

        for line in self._open_file(path_to_file, "r"):
            key, value = self._split_and_check_key(line.rstrip(), "=")
            if value.isdigit():
                self.items[key] = int(value)
            else:
                self.items[key] = value

    def __getitem__(self, item):
        """Returns value by key."""
        return self.items[item]

    def __getattr__(self, item):
        """Returns value by key."""
        return self.items[item]

    def __str__(self) -> str:
        """A function for pretty print"""
        return f"{self.items}"


if __name__ == "__main__":
    path_to_file = "homework8/task1.txt"
    storage = KeyValueStorage(path_to_file)
    print(storage.power)
