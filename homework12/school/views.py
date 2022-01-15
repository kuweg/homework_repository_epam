from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Homework, HomeworkResult
from .services import (check_homework, create_homework, do_homework,
                       reset_homework_results, reset_homework_single_result)


@csrf_exempt
def set_homework(request):
    """
    Function, which adds Homework object into homework table.
    """
    teacher_id = request.POST.get("teacher")
    hometask = request.POST.get("hometask")
    deadline = request.POST.get("deadline")

    for attr in (teacher_id, hometask, deadline):
        if not attr:
            return JsonResponse({"success": False}, status=400)

    teacher_id = int(teacher_id)
    deadline = int(deadline)
    try:
        create_homework(
            homework_task=hometask, deadline_days=deadline, author_id=teacher_id
        )
    except Exception as err:
        return JsonResponse({"success": False, "message": f"{err}"}, status=405)

    return JsonResponse(
        {"success": True, "object": Homework.objects.get(text=hometask).text}
    )


@csrf_exempt
def check_homework_for_being_valid(request):
    """
    Function, which check HomeworkResult object and updates it
    into homeworkresults table.
    """
    homework_res_id = request.POST.get("homework_res")
    teacher_id = request.POST.get("teacher")

    for attr in (teacher_id, homework_res_id):
        if not attr:
            return JsonResponse({"success": False, "message": f"{attr}"}, status=400)

    homework_res_id = int(homework_res_id)
    teacher_id = int(teacher_id)
    try:
        check_homework(homework_res_id, teacher_id)
    except Exception as err:
        return JsonResponse({"success": False, "message": f"{err}"}, status=405)
    return JsonResponse(
        {
            "success": True,
            "acccept": HomeworkResult.objects.get(pk=homework_res_id).is_accepted,
        }
    )


@csrf_exempt
def complete_homework(request):
    """
    Function, which checks Homework object, transoforms it into HomeworkResult
    and puts into homeworkresult table.
    """
    homework_id = request.POST.get("homework")
    student_id = request.POST.get("student")
    solution = request.POST.get("solution")

    for attr in (homework_id, student_id, solution):
        if not attr:
            return JsonResponse({"success": False}, status=400)

    homework_id = int(homework_id)
    student_id = int(student_id)

    try:
        do_homework(homework_id=homework_id, solution=solution, author_id=student_id)
    except Exception as err:
        return JsonResponse(
            {"success": False, "message": f"{err}"}, status=405
            )
    return JsonResponse(
        {
            "Success": True,
            "Solution": HomeworkResult.objects.get(homework=homework_id).solution,
        }
    )


def reset_results(request):
    """
    Function, which nullifies is_accepted field in HomeworkResult object
    which corresponds to passed Homework object.
    Otherwise reset is_acceptace field in all HomeworkResult objects..
    """
    homework_id = request.GET.get("homework")
    if homework_id:
        try:
            reset_homework_single_result(homework_id)
            return JsonResponse({"Success": True})
        except Exception as err:
            return JsonResponse({"success": False, "message": f"{err}"}, status=405)
    else:

        reset_homework_results()
        return JsonResponse({"Success": True})
