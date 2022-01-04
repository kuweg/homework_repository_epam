from school.models import Student, Teacher


def fill_tables():
    student_a: Student = Student.objects.create(
        last_name="Petrov", first_name="Ivan"
    )
    student_b: Student = Student.objects.create(
        last_name="Markov", first_name="Nikolai"
    )
    teacher_a: Teacher = Teacher.objects.create(
        last_name="One", first_name="Teacher"
    )
    teacher_b: Teacher = Teacher.objects.create(
        last_name="Two", first_name="Teacher"
    )

    homework1 = teacher_a.create_homework(
        homework_task="Learn django", deadline_days=5
    )
    homework2 = teacher_a.create_homework(
        homework_task="Write django models", deadline_days=3
    )
    homework3 = teacher_b.create_homework(
        homework_task="Play dota2 all day", deadline_days=1
    )
    homework4 = teacher_b.create_homework(
        homework_task="Eat all salads", deadline_days=2
    )

    result1 = student_a.do_homework(homework1, "Django is cool!")
    result2 = student_a.do_homework(homework2, "No")
    result3 = student_b.do_homework(homework3, "Chin choppa, chin choppa!")
    result4 = student_b.do_homework(homework4, "Help")

    teacher_a.check_homework(result1)
    teacher_a.check_homework(result2)
    teacher_b.check_homework(result3)
    teacher_b.check_homework(result4)
