# I decided to write a code that generates data filtering object
# from a list of keyword parameters:
from typing import Any, Callable, List


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions: Callable):
        self.functions = functions

    def apply(self, data: List[Any]) -> List:
        return [item for item in data if all(i(item) for i in self.functions)]


# example of usage:
# positive_even = Filter(
# lamba a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(int, a)))
# positive_even.apply(range(100)) should return only even numbers from 0 to 99


def make_filter(**keywords) -> Callable:
    """
    Generate filter object for specified keywords
    """
    # does key exist
    # value and value
    # 3d mistake should find

    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(data, _key=key, _value=value):
            if _key in data.keys():
                return data[_key] == _value

        filter_funcs.append(keyword_filter_func)

    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


# make_filter(name='polly', type='bird').apply(sample_data)
# should return only second entry from the list

# There are multiple bugs in this code.
# Find them all and write tests for faulty cases.
