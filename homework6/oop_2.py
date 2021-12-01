"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import abc
import datetime
from collections import defaultdict
from pprint import pprint


class DeadlineError(Exception):
    """
    Error for homework tasks
    which have expired.
    """
    pass


class AlreadyCheckedError(Exception):
    """Error for already checked homework tasks
    to avoid unwanted changes in do_homework dict."""
    pass


class InstanceError(Exception):
    """My error for wrong input type."""
    pass


class Person:
    """Parent class to keep code DRY"""
    def __init__(self, last_name: str, first_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name

    def __repr__(self) -> str:
        return f"'{self.first_name} {self.last_name}'"


class BaseStudent(Person):
    """Class to help clarify that
    some functions may need a Student object, even
    if they initialized before it (forward declaration).
    """
    @abc.abstractmethod
    def do_homework(self, homework, solution):
        raise NotImplementedError

    def __repr__(self) -> str:
        return super().__repr__()


class Homework:
    """Class which contains information about homework."""
    def __init__(self, task_text, deadline) -> None:
        self.text = task_text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        """Checking does a homework still valid."""
        return datetime.datetime.now() < self.created + self.deadline

    def __str__(self) -> str:
        return (
            f"[Text: '{self.text}' | Created: {self.created}"
            + " | Deadline: {self.deadline}]"
        )

    def __repr__(self) -> str:
        return (
            f"[Text: '{self.text}' | Created: {self.created} "
            + f"| Deadline: {self.deadline}]"
        )


class HomeworkResult:
    """Class which contains information about completed
        homework tasks from Homework object.
    """
    def __init__(
            self, author: BaseStudent,
            homework: Homework, solution: str
            ) -> None:

        if not isinstance(homework, Homework):
            raise InstanceError("You gave a not Homework object")

        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = datetime.datetime.now()

    def __repr__(self) -> str:
        return (
            f"[Author: {self.author} | Homework: '{self.homework.text}' "
            + f"| Solution: '{self.solution}']"
        )


class Student(BaseStudent):
    """This class is imitating a simple student behaviour."""

    def do_homework(self, homework: Homework, solution) -> HomeworkResult:
        """Checking Homework object being an actual and
        transfer it to HomeworkResult object.
        """
        if not homework.is_active():
            raise DeadlineError("You are late!")
        return HomeworkResult(self, homework, solution)

    def __repr__(self) -> str:
        return super().__repr__()


class Teacher(Person):
    """This class is imitating a simple teacher behaviour."""

    homework_done = defaultdict(list)
    APPROVING_LENGTH = 5

    @staticmethod
    def create_homework(homework_task, homework_deadline) -> Homework:
        """Homework's instances constructor."""
        return Homework(homework_task, homework_deadline)

    def check_homework(self, homework_res: HomeworkResult) -> bool:
        """Checking HomeworkResult object being valid according
        specified criterias.
        """
        if not isinstance(homework_res, HomeworkResult):
            raise InstanceError("You gave not a HomeworkResult object")

        if homework_res in self.homework_done.values():
            raise AlreadyCheckedError("Homework has been already accepted")

        if len(homework_res.solution) > self.APPROVING_LENGTH:
            self.homework_done[homework_res.homework] = homework_res
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        """
        This method deletes a passed object from a common variable
        or cleans that variable in case of empty input.
        """
        if homework and isinstance(homework, Homework):
            cls.homework_done.pop(homework)
        else:
            cls.homework_done.clear()


if __name__ == "__main__":
    opp_teacher = Teacher("Daniil", "Shadrin")
    advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

    lazy_student = Student("Roman", "Petrov")
    good_student = Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    # advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    opp_teacher.check_homework(result_2)
    opp_teacher.check_homework(result_3)

    print(Teacher.homework_done[oop_hw])
    pprint(Teacher.homework_done)
    Teacher.reset_results()
    print(Teacher.homework_done)
