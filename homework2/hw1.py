"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter, defaultdict
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """
    Finding longest word with largest amount of unique symbols.
    collections.defaultdict() was used:"
    https://docs.python.org/3/library/collections.html#collections.defaultdict
    """
    words_stat = defaultdict()
    with open(file_path, "r", encoding="unicode-escape",
              errors="ignore") as file_handler:
        for line in file_handler:
            for word in line.split():
                words_stat[
                    word.strip(string.punctuation)] = len(set(word))
    sorted_list_with_counts = sorted(
        words_stat.items(), key=lambda k: (k[1], len(k[0])), reverse=True
    )
    ten_longest_words = []
    for pair in sorted_list_with_counts[:10]:
        ten_longest_words.append(pair[0])
    return ten_longest_words


def get_rarest_char(file_path: str) -> str:
    """
    Finding least common char in file.
    collections.defaultdict() was used:"
    https://docs.python.org/3/library/collections.html#collections.defaultdict
    """
    chars_stat = defaultdict(int)
    with open(file_path, "r", encoding="unicode-escape",
              errors="ignore") as file_handler:
        for line in file_handler:
            for char in line:
                chars_stat[char] += 1
    sorted_chars = sorted(chars_stat.items(),
                          key=lambda k: k[1], reverse=False)
    rarest_char = sorted_chars[0][0]
    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    """
    Count punctuation chars in provided file.
    """
    punctuation_counter = 0
    with open(file_path, "r", encoding="unicode-escape",
              errors="ignore") as file_handler:
        for line in file_handler:
            for char in line:
                if char in string.punctuation:
                    punctuation_counter += 1
    return punctuation_counter


def count_non_ascii_chars(file_path: str) -> int:
    """"
    Count a non-ascii chars in file.
    """
    ascii_chars_counter = 0
    with open(file_path, "r", encoding="unicode-escape",
              errors="ignore") as file_handler:
        for line in file_handler:
            for char in line:
                if not char.isascii():
                    ascii_chars_counter += 1
    return ascii_chars_counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """
    Finding the most common non-ascii char in file
    using collections.Counter().
    Documentation:
    https://docs.python.org/3/library/collections.html#collections.Counter
    """
    non_ascii_chars_counter = Counter()
    with open(file_path, "r", encoding="unicode-escape",
              errors="ignore") as file_handler:
        for line in file_handler:
            for char in line:
                if not char.isascii():
                    non_ascii_chars_counter[char] += 1
    most_common_non_ascii_char = non_ascii_chars_counter.most_common()[0][0]
    return most_common_non_ascii_char
