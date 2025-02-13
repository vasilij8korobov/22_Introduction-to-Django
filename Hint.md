1.
Шаги, необходимые для установки виртуального окружения:
    1) Создайте директорию для проекта:
        mkdir myproject
    2) Перейдите в созданную директорию:
        cd myproject
    3) Создайте виртуальное окружение:
        python3 -m venv venv                python -m venv venv
    4) Активируйте виртуальное окружение:
        Для macOS и Linux:
            source venv/bin/activate
        Windows:
            venv\Scripts\activate

2.
Устанавливаем Django:
    pip install django
сохраняем список зависимостей, если используете pip и venv:
    pip freeze > requirements.txt

3.
Инициализация проекта
    Способ №1: Инициализация проекта внутри текущей директории
        django-admin startproject config .
    Способ №2: Инициализация проекта с созданием новой директории
        django-admin startproject (имя проекта)