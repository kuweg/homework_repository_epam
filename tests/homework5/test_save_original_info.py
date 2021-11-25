from homework5.save_original_info import print_result


@print_result
def my_foo(*args):
    """Foo function for sum"""
    return sum(args)


def test_func_docstring():
    assert my_foo.__doc__ == "Foo function for sum"


def test_func_name():
    assert my_foo.__name__ == "my_foo"


def test_original_func():
    original_func = str(my_foo.__original_func)
    assert original_func.startswith("<function my_foo")


def test_print_decorator(capsys):
    my_foo(1, 2)
    capsys_reader = capsys.readouterr()
    assert int(capsys_reader.out) == 3


def test_original_func_id(capsys):
    copy_of_foo = my_foo.__original_func
    assert copy_of_foo is my_foo.__original_func
