import os

from celery import Celery
from celery.schedules import crontab
from constance import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=config.NEWS_MAIL_SCHEDULED_TIME.split(':')[0],
                                     minute=config.NEWS_MAIL_SCHEDULED_TIME.split(':')[1]),
                             'news_and_places.tasks.news.send_news_mail',
                             name='send_news_mail')
