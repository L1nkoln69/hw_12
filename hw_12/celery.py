from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab


app = Celery('hw_12')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw_12.settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'task_celery_beat': {
        'task': 'celery_beat.tasks.parser_for_page',
        'schedule': crontab(minute=0, hour='1-23/2')
    }
}
