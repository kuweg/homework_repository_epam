"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Class decorator
    which counts created class instances.
    """
    setattr(cls, "calls_counter", 0)

    primary_init = cls.__init__

    def __init__(self, *args, **kwargs):
        """Adding to init a counter variable."""
        cls.calls_counter += 1
        primary_init(self, *args, **kwargs)

    def get_created_instances(self=None):
        """Get method for counter variable."""
        return cls.calls_counter

    def reset_instances_counter(self=None):
        """Returns counter value and nullify it."""
        before_cleaning = cls.calls_counter
        cls.calls_counter = 0
        return before_cleaning

    setattr(cls, "__init__", __init__)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
