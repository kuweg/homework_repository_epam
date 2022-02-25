from django.contrib.auth import get_user_model
from django.test import TestCase
from school.models import Homework, HomeworkResult, Student, Teacher

# Create your tests here.
User = get_user_model()


class StudentTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            last_name="Ivanov", first_name="Ivan", username="abc"
        )
        Student.objects.create(user=user)

    def test_student_name(self):
        """Testing that object has correct attributes."""
        student_a: Student = Student.objects.get(id=1)
        self.assertEqual(student_a.user.first_name, "Ivan")
        self.assertEqual(student_a.user.last_name, "Ivanov")


class TeacherTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            last_name="Teacher", first_name="One", username="abcd"
        )
        Teacher.objects.create(user=user, approving_length=5)

    def test_teacher_name(self):
        """Testing that object has correct attributes."""
        teacher_a: Teacher = Teacher.objects.get(id=1)
        self.assertEqual(teacher_a.user.first_name, "One")
        self.assertEqual(teacher_a.user.last_name, "Teacher")
        self.assertEqual(teacher_a.approving_length, 5)


class TestCallsCreateHomework(TestCase):
    def setUp(self):
        user = User.objects.create(
            last_name="Ivanov", first_name="Ivan", username="abc"
        )
        Student.objects.create(user=user)
        user = User.objects.create(
            last_name="Teacher", first_name="One", username="abcd"
        )
        Teacher.objects.create(user=user, approving_length=5)
        Homework.objects.create(
            text="TEST HW", deadline=5, author=Teacher.objects.get(pk=1)
        )

    def test_create_homework_call(self):
        """Testing that homework can be created using post request."""
        data = {"teacher": 1, "hometask": "test me", "deadline": 5}
        resp = self.client.post("/set_homework/", data=data)
        self.assertEqual(resp.status_code, 200)

    def test_complete_homework_call(self):
        """Testing that homework can be complited using post request."""
        data = {"homework": 1, "student": 1, "solution": "hehehehe"}
        resp = self.client.post("/complete_homework/", data=data)
        self.assertEqual(resp.status_code, 200)


class TestCallsCheckHomework(TestCase):
    def setUp(self):
        user = User.objects.create(
            last_name="Ivanov", first_name="Ivan", username="abc"
        )
        Student.objects.create(user=user)
        user = User.objects.create(
            last_name="Teacher", first_name="One", username="abcd"
        )
        Teacher.objects.create(user=user, approving_length=5)
        Homework.objects.create(
            text="TEST HW", deadline=5, author=Teacher.objects.get(pk=1)
        )
        HomeworkResult.objects.create(
            author=Student.objects.get(pk=1),
            homework=Homework.objects.get(pk=1),
            solution="=(_/|_/|_)=",
            is_accepted=0,
        )

    def test_check_homework_call(self):
        """Testing that homework can be checked using post request."""
        data = {"homework_res": 1, "teacher": 1}
        resp = self.client.post("/check_homework_for_being_valid/", data=data)
        self.assertEqual(resp.status_code, 200)

    def test_reset_results(self):
        """
        Testing that is_accepted field can be nullified using get request.
        """
        resp = self.client.get("/reset_results/?homework=1")
        self.assertEqual(resp.status_code, 200)
