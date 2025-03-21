from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'year', 'email', 'enrollment_date', ]

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'first_name'
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'last_name'
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите фамилию'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'email'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите email'  # Текст подсказки внутри поля
        })

        # Настройка атрибутов виджета для поля 'enrollment_date'
        self.fields['enrollment_date'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'type': 'date'  # Указание типа поля как даты
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        suffix = ('@example.com', '@gmail.com', '@mail.ru',)
        if not email.endswith(suffix):
            raise ValidationError(f'Email должен оканчиваться на {suffix}')
        return email

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name and first_name.lower() == last_name.lower():
            self.add_error('last_name', 'Имя и фамилия не могут быть одинаковыми')