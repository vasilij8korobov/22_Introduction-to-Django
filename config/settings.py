"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/

Содержит все основные настройки вашего проекта Django.
Эти настройки включают конфигурацию баз данных, установленные приложения,
настройки статических файлов и многое другое.
"""
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Определяет корневую директорию проекта.
# Этот параметр используется для построения абсолютных путей внутри проекта.


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY'),
# Секретный ключ, используемый для криптографических подписей.
# Необходимо держать его в секрете.


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.getenv('DEBUG') == "True" else False
# Включает или отключает режим отладки. Включен (True) только в процессе разработки.
# При разворачивании на сервере обязательно установить значение False


ALLOWED_HOSTS = []
# Список доменных имен, которые могут обслуживаться вашим приложением.
# На сервере добавьте сюда ваш домен
# Список разрешенных доменов (используйте '*' для разрешения всех)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "Students",
    "library"
    # Ваши собственные приложения
]
"""
INSTALLED_APPS — содержит список всех приложений, активированных в вашем проекте.
Этот список включает как встроенные приложения Django, так и ваши собственные. 
Об этом мы поговорим позже.
"""

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
"""
MIDDLEWARE — список промежуточного ПО, 
которое обрабатывает входящие запросы и выходящие ответы.
"""

ROOT_URLCONF = 'config.urls'
"""
ROOT_URLCONF — указывает на модуль маршрутизации, 
который будет использоваться для маршрутизации URL-адресов в проекте. 
В данном случае это config.urls.
"""

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
"""
TEMPLATES — настройки шаблонизации. Здесь указывается шаблонный двигатель по умолчанию, 
директории для шаблонов и контекстные процессоры, 
которые добавляют переменные в контекст шаблона
"""

WSGI_APPLICATION = 'config.wsgi.application'
"""
WSGI_APPLICATION — указывает путь к WSGI-приложению. 
Это точка входа вашего приложения для совместимости с WSGI-серверами, такими как Gunicorn. 
Настройка необходима в основном при разворачивании на сервере.
"""

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('USER'),
        'PASSWORD': os.getenv('PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT', default='5432'),
    }
}
"""
DATABASES — настройки базы данных. 
По умолчанию используется SQLite, но вы можете настроить и другие базы данных, 
такие как PostgreSQL, MySQL или Oracle.
"""

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
"""
AUTH_PASSWORD_VALIDATORS — список валидаторов, 
используемых для проверки надежности паролей пользователей.
"""

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'  # устанавливает язык для проекта

TIME_ZONE = 'UTC'  # устанавливает часовую зону для проекта.
# Пример для московского времени: TIME_ZONE = 'Europe/Moscow'


USE_I18N = True  # включает поддержку интернационализации.
# USE_L10N — включает поддержку локализации, применяя форматирование даты и времени.
USE_TZ = True  # включает поддержку временных зон.

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'  # содержит информацию о URL для доступа к статическим файлам.
STATICFILES_DIRS = [BASE_DIR / 'static']  # — это список директорий на диске,
# из которых будут подгружаться статические файлы.


MEDIA_URL = '/media/'  # -содержит информацию о URL для доступа к медиафайлам.
MEDIA_ROOT = BASE_DIR / 'media'  # -это директория на диске,
# где будут храниться медиафайлы, загружаемые пользователями.


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
