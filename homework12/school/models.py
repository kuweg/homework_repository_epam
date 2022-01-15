from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Homework(models.Model):
    text = models.CharField(max_length=1000, null=False, blank=True)
    deadline = models.PositiveSmallIntegerField(
        null=False, blank=False, help_text="Days to do homework"
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey("Teacher", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (
            f"[Text: '{self.text}' | Created: {self.created}"
            f" | Deadline: {self.deadline}]"
        )


class HomeworkResult(models.Model):
    author = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="author"
    )
    homework = models.ForeignKey(
        Homework, on_delete=models.CASCADE, related_name="homework_results"
    )
    solution = models.CharField(max_length=125, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_accepted = models.BooleanField(
        default=False, help_text="Define if solution was correct"
    )

    def __str__(self):
        return (
            f"[Author: {self.author} | Homework: '{self.homework.text}'"
            f" | Solution: '{self.solution} |"
            f"is_accepted: {self.is_accepted}']"
        )


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.get_full_name()


class Teacher(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    approving_length = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        default=5,
        help_text="min length of homework for approving",
    )

    def __str__(self) -> str:
        return f"{self.user.get_full_name()}, approve_length <{self.approving_length}>"
