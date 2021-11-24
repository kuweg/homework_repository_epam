import datetime

from homework5.oop_1 import Student, Teacher


student = Student('Nikita', 'Zaitsev')
teacher = Teacher('Ivan', 'Ivanov')
expired_homework = teacher.create_homework('Learn functions', 0)
weekly_homework = teacher.create_homework('Lecture 5', 7)


def test_student_name():
    assert (student.last_name == 'Nikita' and
            student.first_name == 'Zaitsev')


def test_teacher_name():
    assert (teacher.last_name == 'Ivan' and
            teacher.first_name == 'Ivanov')


def test_expired_homework_deadline():
    assert expired_homework.deadline == datetime.timedelta(0)


def test_weekly_homework_deadline():
    assert weekly_homework.deadline == datetime.timedelta(7)


def test_homework_task():
    assert weekly_homework.text == "Lecture 5"


def test_expired_homework_message():
    assert student.do_homework(expired_homework) is None


def test_homework_deadline_positive():
    assert (student.do_homework(weekly_homework) == weekly_homework)
