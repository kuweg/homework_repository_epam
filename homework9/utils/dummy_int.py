import os
import random
from typing import Any, Callable


class DummyIntegers:
    """
    Class for creating any amount of files
    with random integers.

    :param n_files: amount of files
    :type n_files: int
    :param template_name: template name for  '.txt' files
    :type template_name: str
    :param file_size: amount of rows in file
    :type file_size: int
    :param seed: use random.seed(0) to generate same values
    :type seed: bool
    """
    def __init__(self, n_files: int,
                 template_name: str,
                 file_size: int,
                 seed: bool = True) -> None:

        self.n_files = n_files
        self.template_name = template_name
        self.file_size = file_size
        self.cwd = os.getcwd()
        if seed:
            random.seed(0)

    def create_dummies(self):
        """
        Creating dummie diles in current directory.
        """
        os.chdir(self.cwd)
        for i in range(self.n_files):
            random_numbers = sorted(
                random.sample(range(0, 11), self.file_size)
                )
            with open(self.template_name + str(i) + ".txt", "w") as file:
                file.write("\n".join(str(number) for number in random_numbers))

    def remove_dummies(self):
        """
        Removing created files.
        """
        for i in range(self.n_files):
            os.remove(self.template_name + str(i) + ".txt")

    def get_paths(self, dir=None):
        """
        Returns list of created files.
        If more comples path needed put path prefix to dir.

        :param dir: for more complex path
        :type dir: str
        :return: list of file paths
        :rtype: list
        """
        if dir:
            return [
                (dir + "/" + self.template_name + str(i) + ".txt")
                for i in range(self.n_files)
            ]
        return [
            self.template_name + str(i) + ".txt"
            for i in range(self.n_files)
            ]

    def __call__(self, func: Callable) -> Any:
        """
        Decorator attempt.
        """
        def wrapper(*args, **kwargs):
            self.create_dummies()
            res = func(*args, **kwargs)
            self.remove_dummies()
            return res

        return wrapper
