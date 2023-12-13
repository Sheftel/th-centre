from datetime import date

from django.core.mail import send_mass_mail
from constance import config

from app import celery_app
from ..models import News
"""
    Вопросы:
        1. Как выдавать информацию о новостях за день, если текст сообщения в constance статичен?
        2. В каком формате выдавать новости?
"""


@celery_app.task
def send_news_mail():
    news_for_today = News.objects.filter(created_at__date=date.today()).order_by('-created_at').values_list('title', flat=True).all()[:10]
    send_mass_mail((
        (config.NEWS_MAIL_SUBJECT,
         config.NEWS_MAIL_TEXT+'\n'.join(news_for_today),
         'from@mail.com',
         config.NEWS_MAIL_RECIPIENTS.split(','),),
    ))
