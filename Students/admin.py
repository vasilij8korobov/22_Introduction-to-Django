from django.contrib import admin
from .models import Student


# admin.site.register(Student) - простой короткий вариант регистрации классов модели в админе
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'year',)
    list_filter = ('year',)
    search_fields = ('first_name', 'last_name',)
    """
    более гибкий способ регистрации
    """
