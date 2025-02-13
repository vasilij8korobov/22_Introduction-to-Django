#!/usr/bin/env python
"""Утилита командной строки Django для административных задач."""
import os
import sys


def main():
    """Выполнить административные задачи."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Вы уверены, что он установлен и"
            "доступен в переменной окружения PYTHONPATH?"
            "Вы забыли активировать виртуальную среду?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


""" 
Примеры команд
    Запуск сервера разработки:
        python manage.py runserver
        
    Применение миграций:
        python manage.py migrate
        
    Создание нового приложения:
        python manage.py startapp app_name
        
"""