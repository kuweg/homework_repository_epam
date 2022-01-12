from django.utils.timezone import now, timedelta

from .errors import (AlreadyAcceptedError, DeadlineError, DoesNotExistError,
                     InstanceError)
from .models import Homework, HomeworkResult, Student, Teacher


def _is_active(homework: Homework):
    """Checking does homework active."""
    return now() < homework.created + timedelta(days=homework.deadline)


def _mark_as_accepted(homework_res: HomeworkResult):
    """Marking homework in table if it's accepted."""
    homework_res.is_accepted = True
    homework_res.save()


def _reset_mark(homework_res: HomeworkResult):
    """Removing acceptance mark if needed."""
    homework_res.is_accepted = False
    homework_res.save()


def _get_object_by_id(obj, id):
    """
    Trying to get an object by its primary key.
    Raises DoesNotExistError if that object does not exists."""
    try:
        return obj.objects.get(pk=id)
    except DoesNotExistError as exp:
        raise exp('There is no object with passed id')


def do_homework(homework_id: int,
                solution: str,
                author_id: int) -> HomeworkResult:
    """
        Converting Homework object at HomeworkResut object,
        pretending that student compeleted homework.

        :param homework: a homework object
        :type homework: Homework
        :param solution: student's solution
        :type solution: str
        :param author: author of solution
        :type author: Student
        :raise: Instance error if passed homework is not Homework,
                DeadlineError if homework's deadline was passed.
        :return: result of homework
        :rtype: HomeworkResult
    """
    homework = _get_object_by_id(Homework, homework_id)
    student = _get_object_by_id(Student, author_id)
    if not isinstance(homework, Homework):
        raise InstanceError("Homework should be a Homework object")

    if not _is_active(homework):
        raise DeadlineError("You are late!")

    return HomeworkResult.objects.create(
            author=student, homework=homework, solution=solution
        )


def create_homework(homework_task: str,
                    deadline_days: int,
                    author_id: int) -> Homework:
    """
        Creating homework object.
        :param homework_task: task for homework
        :type homework_task: str
        :param deadline_days: days for complete homework
        :type deadline_days: int
        :param author: author of homework
        :type author: Teacher
        :return: a homework
        :rtype: Homework
    """
    teacher = _get_object_by_id(Teacher, author_id)

    return Homework.objects.create(
        text=homework_task, deadline=deadline_days, author=teacher
    )


def check_homework(homework_res_id: int, teacher_id: int) -> bool:
    """
        Checking student's solution beign greater than declared lenght.
        Create mark at homework table

        :param homework_res: student's homework solution
        :type homework_res: HomeworkResult
        :param aproving_length: criteria for homework acceptance
        :type aproving_length: int
        :raise: InstanceError if student's solution is not a
                HomeworkResult object.
                AlreadyAcceptedError if homework was accepted in past.
        :return: True if solution is valid, otherwise False
        :rtype: bool
    """
    homework_res = _get_object_by_id(HomeworkResult, homework_res_id)

    if homework_res.is_accepted:
        raise AlreadyAcceptedError("Homework has already been accepted")

    teacher = _get_object_by_id(Teacher, teacher_id)
    aproving_length = teacher.aproving_length
    if len(homework_res.solution) > aproving_length:
        _mark_as_accepted(homework_res)
        return True
    return False


def reset_homework_results(homework_id: int):
    """
        Reseting 'is_accepted' mark in homework_result table
        for passed homework, otherwise for all.

        :param homework: homework object
        :type homework: Homework
    """
    homework = _get_object_by_id(Homework, homework_id)
    if homework and isinstance(homework, Homework):
        homework.homework_results.update(is_accepted=False)
    else:
        HomeworkResult.objects.update(is_accepted=False)
