from django.core.mail import send_mass_mail
from constance import config

from app import celery_app

"""
    Вопросы:
        1. Как выдавать информацию о новостях за день, если текст сообщения в constance статичен?
        2. В каком формате выдавать новости?
"""


@celery_app.task
def send_news_mail():
    send_mass_mail((
        (config.NEWS_MAIL_SUBJECT,
         config.NEWS_MAIL_TEXT,
         'from@mail.com',
         config.NEWS_MAIL_RECIPIENTS.split(','),),
    ))
