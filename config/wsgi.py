"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

"""
Содержит настройки для серверного интерфейса WSGI
(Web Server Gateway Interface). 
WSGI используется для взаимодействия между вашим проектом Django и 
веб-сервером, таким как Gunicorn или uWSGI. 
Обычно этот файл не требует дополнительных настроек.
"""