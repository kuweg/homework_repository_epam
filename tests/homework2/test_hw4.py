from homework2.hw4 import cache


def test_positive_case1():
    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    assert val_1 is val_2


def test_negative_case():
    def func(a, b):
        return (a ** b) ** 2

    def func2(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)
    cache_func2 = cache(func2)
    some = 100, 200
    val_1 = cache_func(*some)
    val_2 = cache_func2(*some)
    assert val_1 is not val_2
