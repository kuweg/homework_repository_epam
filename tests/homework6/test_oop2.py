import pytest

from homework6.oop_2 import (AlreadyCheckedError, DeadlineError, Homework,
                             HomeworkResult, InstanceError, Student, Teacher)

# Creating two teachers
opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

# Creating two students
lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

# Creating two homeworks
oop_hw = opp_teacher.create_homework("Learn OOP", 1)
docs_hw = opp_teacher.create_homework("Read docs", 5)

# Let our students do a homeworks
result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
# This one is too short and won't be accepted
result_3 = lazy_student.do_homework(docs_hw, "done")

# First teacher will check them
opp_teacher.check_homework(result_1)
opp_teacher.check_homework(result_2)
opp_teacher.check_homework(result_3)


def test_shared_variable():
    temp_1 = opp_teacher.homework_done
    assert temp_1 == Teacher.homework_done


def test_instance_after_do_homework():
    assert isinstance(result_1, HomeworkResult) is True


def test_deadline_error():
    false_hw = Homework("Test function", 0)
    with pytest.raises(DeadlineError):
        good_student.do_homework(false_hw, "trying my best")


def test_instance_homework_error():
    with pytest.raises(InstanceError):
        opp_teacher.check_homework("Error")


def test_error_existing_homework():
    with pytest.raises(AlreadyCheckedError):
        advanced_python_teacher.check_homework(result_1)


def test_homework_done():
    assert len(Teacher.homework_done) == 2


def test_reset_results():
    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0
