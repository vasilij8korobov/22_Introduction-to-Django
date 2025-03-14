from django.http import HttpResponse
from django.shortcuts import render

from Students.models import Student


def example_view(request):
    return render(request, 'app/example.html')


def show_data(request):
    if request.method == 'GET':
        return render(request, 'app/show_data.html')


def submit_data(request):
    # request.GET   - это словари хранящие в себе GET(получить)
    # request.POST  - и POST(отправить) параметры запроса соответственно.
    if request.method == 'POST':
        return HttpResponse("Данные отправлены")


def show_item(request, item_id):
    return render(request, 'app/item.html', {'item_id': item_id})


def about(request):
    return render(request, 'Students/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}! Сообщение получено.')
    return render(request, 'Students/contact.html')


def index(request):
    student = Student.objects.get(id=1)
    context = {
        'student_name': f"{student.first_name} {student.last_name}",
        'student_year': student.get_year_display(),
    }
    return render(request, 'Students/index.html', context=context)


def student_detail(request):
    student = Student.objects.get(id=1)
    context = {
        'student': student,
    }
    return render(request, 'Students/student_detail.html', context=context)


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'Students/student_list.html', context)