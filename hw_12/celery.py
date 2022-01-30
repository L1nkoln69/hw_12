from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_12.settings')

app = Celery("hw_12")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'parsing-site': {
        'task': 'hw_celery.tasks.parsing_site',
        'schedule': crontab(minute='*/15')
    }
}
