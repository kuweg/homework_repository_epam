from django.test import TestCase
from school.errors import AlreadyAcceptedError, InstanceError
from school.models import Student, Teacher

# Create your tests here.


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(last_name="Ivanov", first_name="Ivan")

    def test_student_name(self):
        """Testing that object has correct attributes."""
        student_a: Student = Student.objects.get(id=1)
        self.assertEqual(student_a.first_name, "Ivan")
        self.assertEqual(student_a.last_name, "Ivanov")


class TeacherTestCase(TestCase):
    def setUp(self):
        Teacher.objects.create(last_name="Teacher", first_name="One")

    def test_teacher_name(self):
        """Testing that object has correct attributes."""
        teacher_a: Teacher = Teacher.objects.get(id=1)
        self.assertEqual(teacher_a.first_name, "One")
        self.assertEqual(teacher_a.last_name, "Teacher")


class HomeworkTestCase(TestCase):
    def setUp(self):
        Student.objects.create(last_name="Ivanov", first_name="Ivan")
        Teacher.objects.create(last_name="Teacher", first_name="One")

    def test_homework_is_active(self):
        """Testing that homework is active."""
        teacher_a: Teacher = Teacher.objects.get(id=1)
        homework1 = teacher_a.create_homework("Test django app", 1)
        self.assertEqual(homework1.is_active(), True)

    def test_homework_author(self):
        """Testing that homewprk author matches with teacher."""
        teacher_a: Teacher = Teacher.objects.get(id=1)
        homework1 = teacher_a.create_homework("Test django app again", 1)
        self.assertEqual(homework1.author, teacher_a)

    def test_complete_homework(self):
        """Testing that student can complete homework."""
        student_a: Student = Student.objects.get(id=1)
        teacher_a: Teacher = Teacher.objects.get(id=1)
        homework1 = teacher_a.create_homework("Test django app", 1)

        result1 = student_a.do_homework(homework1, "Test django")
        self.assertEqual(result1.is_accepted, False)

        teacher_a.check_homework(result1)
        self.assertEqual(result1.is_accepted, True)

    def test_failed_homework(self):
        """Testing that homework could be completed wrong."""
        student_a: Student = Student.objects.get(id=1)
        teacher_a: Teacher = Teacher.objects.get(id=1)
        homework1 = teacher_a.create_homework("Test django app", 1)

        result1 = student_a.do_homework(homework1, "NO")
        self.assertEqual(result1.is_accepted, False)
        teacher_a.check_homework(result1)
        self.assertEqual(result1.is_accepted, False)

    def test_already_accepted_error(self):
        """Testing that teacher won't accept already accepted homework."""
        student_a: Student = Student.objects.get(id=1)
        teacher_a: Teacher = Teacher.objects.get(id=1)
        homework1 = teacher_a.create_homework("Test django app", 1)
        result1 = student_a.do_homework(homework1, "complete")
        teacher_a.check_homework(result1)
        with self.assertRaises(AlreadyAcceptedError) as ex:
            teacher_a.check_homework(result1)
        self.assertEqual(ex.exception.__class__, AlreadyAcceptedError)

    def test_instance_errors(self):
        """Testing InstanceError in Student and Teacher models."""
        student_a: Student = Student.objects.get(id=1)
        teacher_a: Teacher = Teacher.objects.get(id=1)
        with self.assertRaises(InstanceError) as ex:
            student_a.do_homework(123123, "complete")

        self.assertEqual(ex.exception.__class__, InstanceError)

        with self.assertRaises(InstanceError) as ex:
            teacher_a.check_homework("homework")

        self.assertEqual(ex.exception.__class__, InstanceError)

    def test_reset_results(self):
        """Testing that teacher can cancel accepted homework."""
        student_a: Student = Student.objects.get(id=1)
        teacher_a: Teacher = Teacher.objects.get(id=1)
        homework1 = teacher_a.create_homework("Test django app", 1)
        result1 = student_a.do_homework(homework1, "complete")
        self.assertEqual(result1.is_accepted, False)
        teacher_a.check_homework(result1)
        self.assertEqual(result1.is_accepted, True)
        teacher_a.reset_results(homework1)
        self.assertEqual(
            any(
                homework1.homework_results.values_list(
                    "is_accepted",
                    flat=True
                )
            ),
            False
        )
