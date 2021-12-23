import os
import random
from typing import Any, Callable


class DummyIntegers:
    """
    Class for creating any amount of files
    with random integers, one per row.

    :param n_files: amount of files
    :type n_files: int
    :param template_name: template name for  '.txt' files
    :type template_name: str
    :param file_size: amount of rows in file
    :type file_size: int
    :param range_args: args for integer generator
    :type range_args: tuple
    :param seed: use random.seed(0) to generate same values
    :type seed: bool
    """
    def __init__(self, n_files: int,
                 template_name: str,
                 file_size: int,
                 range_args: tuple = (0, 11),
                 seed: bool = True) -> None:

        self.template_name = template_name
        self.file_size = file_size
        self.cwd = os.getcwd() + '/'
        self.file_list = [
            self.cwd + self.template_name + str(order) + ".txt"
            for order in range(n_files)
        ]
        self.range_args = range_args
        if seed:
            random.seed(0)

    def create_dummies(self):
        """
        Creating dummy files in current directory.
        """
        os.chdir(self.cwd)
        for file in self.file_list:
            random_numbers = sorted(
                random.sample(range(*self.range_args), self.file_size)
                )
            with open(file, "w") as file_handler:
                file_handler.write(
                    "\n".join(str(number) for number in random_numbers)
                    )

    def remove_dummies(self):
        """
        Removing created files.
        """
        for file in self.file_list:
            os.remove(file)

    def get_paths(self):
        """
        Returns list of created files.
        """
        return self.file_list

    def __call__(self, func: Callable) -> Any:
        """
        Using class object as decorator for functions.
        Creating a temporary files for function needs
        and deleting them after.
        """
        def wrapper(*args, **kwargs):
            self.create_dummies()
            res = func(*args, **kwargs)
            self.remove_dummies()
            return res

        return wrapper
