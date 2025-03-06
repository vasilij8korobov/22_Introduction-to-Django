Модель — это основа данных приложения в Django. Она представляет собой класс, который наследуется от базового класса
models.Model, и используется для описания структуры и поведения данных, которые будут храниться в базе данных. Каждая модель
соответствует таблице в базе данных.

В Django модель определяет:

поля — колонки таблицы базы данных;
методы — логику взаимодействия с данными.

Пример создания модели данных
Модель всегда создается в специальном файле models.py, который располагается в каждом приложении и автоматически генерируется при создании приложения.

Рассмотрим пример создания простой модели Student, которая будет хранить информацию о студентах:

from django.db import models

class Student(models.Model):
first_name = models.CharField(max_length=150, verbose_name='Имя')
last_name = models.CharField(max_length=150, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name']

Разберемся подробнее, как устроена модель, а также рассмотрим, какие поля могут быть у модели данных.

Базовые настройки модели 
Метод __str__ определяет строковое представление объекта. 
Это полезно для отображения объектов в админке или при выводе на консоль. Он должен возвращать строку, 
которая представляет объект.

Пример:

def __str__(self):
    return f'{self.first_name} {self.last_name}'

Когда мы вызовем

print(student), где student — это объект класса Student, будет выведено значение, 
возвращаемое методом __str__.

Класс Meta используется для добавления метаданных к модели. 
Он определяет такие свойства, как порядок сортировки, наименование
модели в единственном и множественном числе и другие.

Давайте рассмотрим несколько часто используемых атрибутов класса Meta:

verbose_name и verbose_name_plural — определяют отображаемое имя модели в единственном и множественном числе.

class Meta:
    verbose_name = 'Студент'
    verbose_name_plural = 'Студенты'

ordering — определяет порядок сортировки объектов при выборке из базы данных.

class Meta:
    ordering = ['last_name']

db_table — указывает имя таблицы в базе данных, к которой привязана модель. Если параметр не указан, 
Django использует имя модели в нижнем регистре.

class Meta:
    db_table = 'custom_table_name'

Поля моделей
Поля в моделях определяют тип данных, которые будут храниться в базе данных. Django предоставляет множество типов полей
для различных данных.

Полную информацию о типах полей и параметрах можно изучить в документации Django «Справочник типов
полей»: https://django.fun/docs/.

Основные типы полей

CharField — поле для хранения строк.
name = models.CharField(max_length=100)

IntegerField — поле для хранения целых чисел.
age = models.IntegerField()

BooleanField — поле для хранения булевых значений (True/False).
is_active = models.BooleanField(default=True)

TextField — поле для хранения больших текстов.
description = models.TextField()

DateTimeField — поле для хранения даты и времени.
created_at = models.DateTimeField(auto_now_add=True)

ImageField — поле для хранения информации о загруженных изображениях.
image = models.ImageField(upload_to='images/')

Для работы с полем ImageField необходимо установить библиотеку Pillow. Ниже мы расскажем, как работать с этим полем.

ForeignKey — поле для создания внешнего ключа на другую модель.
group = models.ForeignKey(Group, on_delete=models.CASCADE)

OneToOneField — поле для создания связи «один к одному».
profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

ManyToManyField — поле для создания связи «многие ко многим».
tags = models.ManyToManyField(Tag)


Параметры полей

Поля моделей в Django могут принимать различные параметры, которые определяют их поведение и свойства. Рассмотрим
основные параметры, которые могут быть переданы в поля моделей.

Основные параметры
max_length — максимальная длина строки (обязательны для поля типа CharField).
name = models.CharField(max_length=100)

default — значение по умолчанию для поля.
is_active = models.BooleanField(default=True)

null — определяет, может ли поле принимать значение NULL(для всех типов полей, кроме полей с отношениями).
middle_name = models.CharField(max_length=100, null=True)

blank — определяет, может ли поле быть пустым в формах. Полезно для валидации данных.
nickname = models.CharField(max_length=100, blank=True)

choices — ограничивает возможные значения поля. Используется для создания выпадающих списков.

STATUS_CHOICES = [
('draft', 'Draft'),
('published', 'Published'),
]

status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

unique — указывает, что значение поля должно быть уникальным во всей таблице.
email = models.EmailField(unique=True)

verbose_name — читаемое имя поля, отображаемое в админке.
first_name = models.CharField(max_length=100, verbose_name='Имя')

help_text — текст подсказки для поля, отображаемый в админке. 
age = models.IntegerField(help_text='Введите возраст студента')

Параметры для полей с отношениями

on_delete — определяет поведение при удалении связанного объекта (для ForeignKey, OneToOneField и ManyToManyField).
group = models.ForeignKey(Group, on_delete=models.CASCADE)

В параметре on_delete можно использовать следующие значения:

CASCADE — удаляет все связанные записи.
PROTECT — запрещает удаление связанных записей.
SET_NULL — устанавливает значение поля в NULL, если поле позволяет NULL.
SET_DEFAULT — устанавливает значение по умолчанию.
SET() — устанавливает конкретное значение или вызывает функцию для установки значения.
DO_NOTHING — ничего не делает при удалении связанных записей.
related_name — имя для обратного отношения, используется для доступа к связанным объектам.
 
group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
Параметры для полей с датами
 
auto_now_add — устанавливает дату и время создания объекта. 
Значение поля автоматически устанавливается только при создании объекта и больше не изменяется.
created_at = models.DateTimeField(auto_now_add=True)
 
auto_now — устанавливает дату и время при каждом сохранении объекта. 
Значение поля автоматически обновляется при каждом вызове метода save().
updated_at = models.DateTimeField(auto_now=True)

Поля для хранения файлов 
В Django существует набор полей, которые отвечают за хранение файлов, которые загружает пользователь. 
Для них важно указать набор настроек вне модели.

Настройки для хранения файлов

В файле settings.py нужно определить пути для хранения медиафайлов:

# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL — URL-адрес, по которому будут доступны загруженные файлы.
MEDIA_ROOT — путь к директории, где будут храниться загруженные файлы.
Обратите внимание на расстановку слешей при настройке параметров. В URL слеши ставятся до и после 
media. А в директории не ставится ни один слеш — они будут добавлены автоматически библиотекой os.


Также нужно настроить обработку вывода медиафайлов для сервера разработки в файле urls.py вашего проекта:

# config/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Другие URL-пути вашего проекта
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Эти настройки позволяют серверу разработки обрабатывать и выводить загруженные файлы через URL-адрес, указанный в 
MEDIA_URL.

Как работать с полем ImageField
Установка библиотеки Pillow
Для работы с полем ImageField необходимо установить библиотеку Pillow, которая обеспечивает поддержку работы с изображениями:

pip install Pillow
После установки библиотеки не забудьте обновить файл с зависимостями проекта:

pip freeze > requirements.txt
Теперь ваши модели могут использовать поле ImageField для хранения изображений.

Пример использования поля для хранения файлов
Допустим, мы хотим добавить поле для хранения фотографии студента в модель Student. Для этого мы используем поле 
ImageField:

class Student(models.Model):
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR = 'fourth'

    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс'),
    ]

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    year = models.CharField(
        max_length=6,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FIRST_YEAR,
        verbose_name='Курс'
    )
    photo = models.ImageField(upload_to='photos/', verbose_name='Фотография')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name']
В этом примере поле photo будет хранить путь к загруженной фотографии студента, 
а сами файлы будут сохраняться в директорию media/photos/.

Пример использования ForeignKey
Предположим, у нас есть две модели: 
Student и Group. Каждый студент принадлежит определенной группе. 
Здесь имеет смысл установить отношение «многие к одному» (много студентов могут принадлежать одной группе):

from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name

Рассмотрим подробнее аргументы поля ForeignKey:

to — модель, на которую указывает внешний ключ (Group).
on_delete — указывает, что делать с записями в текущей модели, если связанная запись будет удалена.
related_name — имя для обратного отношения. Например, group.students.all() вернет всех студентов группы.
related_query_name — имя для использования в запросах.
Например, Group.objects.filter(students__name='Some Student').

Таким образом, ForeignKey помогает установить и управлять отношениями между моделями в Django, 
делая работу с данными более удобной и структурированной.