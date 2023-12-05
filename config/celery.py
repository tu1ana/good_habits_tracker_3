# celery.py
# absolute_import используется для решения проблемы циклического импорта: мы лезем в settings.py из этого файла, а сам settings.py в свою очередь тоже имеет настройки celery, поэтому может быть циклический импорт
# unicode_literals используется для корректной обработки символов в юникоде
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('config')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()