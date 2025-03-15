from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from Students.models import Student, MyModel

"""ниже идут CBV контроллеры"""


class MyModelCreateView(CreateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'Students/mymodel_form.html'
    success_url = reverse_lazy('Students:mymodel_list')

    def form_valid(self, form):
        """
        form_valid() — используется для обработки данных,
        если форма прошла валидацию.
        Этот метод вызывается после успешной валидации формы и
        сохранения данных
        """
        form.instance.created_by = self.request.user

        return super().form_valid(form)

    def form_invalid(self, form):
        """
        form_invalid() — используется для обработки данных,
        если форма не прошла валидацию.
        Этот метод вызывается при ошибках валидации формы
        """
        response = super().form_invalid(form)
        response.context_data['error_message'] = 'Please correct the errors'

        return response


class MyModelListView(ListView):
    model = MyModel
    template_name = 'Students/mymodel_list.html'
    context_object_name = 'mymodels'

    def get_queryset(self):
        """
        get_queryset() — используется для получения набора данных,
        который будет отображаться в представлении.
        Этот метод позволяет настроить выборку данных из базы данных
        """
        queryset = super().get_queryset().filter(is_active=True)
        return queryset


class MyModelDetailView(DetailView):
    model = MyModel
    template_name = 'Students/mymodel_detail.html'
    context_object_name = 'mymodel'

    def get_additional_data(self):
        return 'Это дополнительная информация'

    def get_context_data(self, **kwargs):
        """
        get_context_data() — используется для добавления данных в контекст шаблона.
        Этот метод позволяет передавать дополнительные данные в шаблон для рендеринга
        """
        context = super().get_context_data(**kwargs)
        context['additional_data'] = self.get_additional_data()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_active:
            raise Http404('Object not found')
        return obj


class MyModelUpdateView(UpdateView):
    model = MyModel
    fields = ['name', 'description']
    template_name = 'Students/mymodel_form.html'
    success_url = reverse_lazy('Students:mymodel_list')


class MyModelDeleteView(DeleteView):
    model = MyModel
    template_name = 'Students/mymodel_confirm_delete.html'
    success_url = reverse_lazy('Students:mymodel_list')


"""ниже идут FBV"""


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


def student_detail(request, student_id):
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
