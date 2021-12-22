"""
Write a function that takes directory path
a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Search for files with specific extension in provided directory.
    Counts tokens in group of files if tokenizer was passed.
    Counts lines in all files if tokenizer is None.

    :param dir_path: path to directory with files:
    :type dir_path: str
    :param file_extension: file extension to find
    :type file_extension: str
    :param tokenizer: a tokenizer object
    :type tokenizer: any callable object
    :return: count of tokens or counr of lines
    in all files in provided directory
    :rtype: int
    """

    files = [
        file for file in dir_path.iterdir()
        if file.suffix == f".{file_extension}"
        ]

    if not files:
        return 0

    counter = sum(
        count_all_tokens(file_path, tokenizer)
        for file_path in files
        )
    return counter


def count_tokens(line, tokenizer: Callable = None):
    """
    Counts all tokens in line if there is token.
    Counts line if token is None

    :param line: text line
    :type line: str
    :param tokenizer: a tokenizer object
    :type tokenizer: any callable object
    :return: count of tokens or count of line
    :rtype: integer
    """

    if tokenizer:
        return sum(1 for _ in tokenizer(line))
    return 1


def count_all_tokens(file_path: str, tokenizer: Callable = None):
    """
    Opens file and counts tokens in each line if tokenizer was passed.
    Counts line in file in tokenizer is None.

    :param file_path: a path to file
    :type file_path: str
    :param tokenizer: a tokenizer object
    :type tokenizer: any callable object
    :return: counts of tokens in file or count of linesS
    :rtype: int
    """

    with open(file_path, "r") as file:
        tokens_counter = sum(count_tokens(line, tokenizer) for line in file)
    return tokens_counter


if __name__ == "__main__":
    cwd = os.getcwd() + "/homework9"
    cwd = Path(cwd)
    b = universal_file_counter(cwd, "txt", str.split)
    print(b)
