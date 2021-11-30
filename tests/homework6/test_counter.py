from homework6.counter import instances_counter


@instances_counter
class Foo:
    pass


@instances_counter
class Dog:
    def __init__(self, bark) -> None:
        self.bark = bark

    def get_bark(self):
        return self.bark


def test_foo_empty_counter():
    assert Foo.get_created_instances() == 0


def test_foo_four_calls():
    _, _, _, _ = Foo(), Foo(), Foo(), Foo()
    assert Foo.get_created_instances() == 4


def test_foo_fifth_call():
    five = Foo()
    assert five.get_created_instances() == 5


def test_foo_reseting_counter():
    assert Foo.reset_instances_counter() == 5
    assert Foo.get_created_instances() == 0


def test_dog_empty_counter():
    assert Dog.get_created_instances() == 0


def test_dog_init_contains_counter():
    _ = Dog("bark!")
    print(Dog.__dict__)
    assert "calls_counter" in Dog.__dict__


def test_dog_single_call():
    assert Dog.get_created_instances() == 1


def test_dog_two_more_calls():
    _, _ = Dog("baark!"), Dog("waff!")
    assert Dog.get_created_instances() == 3


def test_dog_reseting_counter():
    assert Dog.reset_instances_counter() == 3
    assert Dog.get_created_instances() == 0
