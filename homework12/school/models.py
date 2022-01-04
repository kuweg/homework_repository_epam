from typing import Optional

from django.db import models
from django.utils.timezone import now, timedelta

from .errors import AlreadyAcceptedError, DeadlineError, InstanceError


class Person(models.Model):
    first_name = models.CharField(max_length=125, null=False, blank=False)
    last_name = models.CharField(max_length=125, null=False, blank=False)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Homework(models.Model):
    text = models.CharField(max_length=1000, null=False, blank=True)
    deadline = models.PositiveSmallIntegerField(
        null=False, blank=False, help_text="Days to do homework"
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey("Teacher", on_delete=models.CASCADE)

    def is_active(self):
        """Checking does homework active."""
        return now() < self.created + timedelta(days=self.deadline)

    def __str__(self) -> str:
        return (
            f"[Text: '{self.text}' | Created: {self.created}"
            + f" | Deadline: {self.deadline}]"
        )


class HomeworkResult(models.Model):
    author = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="homework_results"
    )
    homework = models.ForeignKey(
        Homework, on_delete=models.CASCADE, related_name="homework_results"
    )
    solution = models.CharField(max_length=125, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_accepted = models.BooleanField(
        default=False, help_text="Define if solution was correct"
    )

    def mark_as_accepted(self):
        """Marking homework in table if it's accepted."""
        self.is_accepted = True
        self.save()

    def reset_mark(self):
        """Removing acceptance mark if needed."""
        self.is_accepted = False
        self.save()

    def __str__(self):
        return (
            f"[Author: {self.author} | Homework: '{self.homework.text}'" +
            f" | Solution: '{self.solution} |" +
            f"is_accepted: {self.is_accepted}']"
        )


class Student(Person):
    def do_homework(self, homework: Homework, solution: str) -> HomeworkResult:
        """
        Converting Homework object at HomeworkResut object,
        pretending that student compeleted homework.

        :param homework: a homework object
        :type homework: Homework
        :param solution: student's solution
        :type solution: str
        :raise: Instance error if passed homework is not Homework,
                DeadlineError if homework's deadline was passed.
        :return: result of homework
        :rtype: HomeworkResult
        """
        if not isinstance(homework, Homework):
            raise InstanceError("Homework should be a Homework object")

        if not homework.is_active():
            raise DeadlineError("You are late!")

        return HomeworkResult.objects.create(
            author=self, homework=homework, solution=solution
        )


class Teacher(Person):
    APPROVING_LENGTH = 5

    def create_homework(self,
                        homework_task: str,
                        deadline_days: int
                        ) -> Homework:
        """
        Creating homework object.
        :param homework_task: task for homework
        :type homework_task: str
        :param deadline_days: days for complete homework
        :type deadline_days: int
        :return: a homework
        :rtype: Homework
        """
        return Homework.objects.create(
            text=homework_task, deadline=deadline_days, author=self
        )

    def check_homework(self, homework_res: HomeworkResult) -> bool:
        """
        Checking student's solution beign greater than declared lenght.
        Create mark at homework table

        :param homework_res: student's homework solution
        :type homework_res: HomeworkResult
        :raise: InstanceError if student's solution is not a
                HomeworkResult object.
                AlreadyAcceptedError if homework was accepted in past.
        :return: True if solution is valid, otherwise False
        :rtype: bool
        """
        if not isinstance(homework_res, HomeworkResult):
            raise InstanceError("This is not a HomeworkResult object")

        if homework_res.is_accepted:
            raise AlreadyAcceptedError("Homework has already been accepted")

        if len(homework_res.solution) > self.APPROVING_LENGTH:
            homework_res.mark_as_accepted()
            return True
        return False

    @staticmethod
    def reset_results(homework: Optional[Homework]):
        """
        Reseting 'is_accepted' mark in homework_result table
        for passed homework, otherwise for all.

        :param homework: homework object
        :type homework: Homework
        """
        if homework and isinstance(homework, Homework):
            homework.homework_results.update(is_accepted=False)
        else:
            HomeworkResult.objects.update(is_accepted=False)
