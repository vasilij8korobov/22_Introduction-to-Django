from django.http import HttpResponse
from django.shortcuts import render


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

