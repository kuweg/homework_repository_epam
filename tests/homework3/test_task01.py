from homework3.task01 import cache


def test_same_outputs():
    @cache(times=2)
    def foo(a, b):
        return a * b

    first_call = foo(1, 2)
    second_call = foo(1, 2)
    assert first_call is second_call


def test_different_outputs():
    @cache(times=2)
    def foo(a, b):
        return a * b

    first_call = foo(1, 2)
    second_call = foo(2, 3)
    assert first_call is not second_call


def test_overflowing_cache():
    @cache(times=2)
    def foo(a, b):
        return a * b

    _ = foo(1, 2)
    second_call = foo(1, 2)
    third_call = foo(1, 2)
    assert second_call is not third_call
