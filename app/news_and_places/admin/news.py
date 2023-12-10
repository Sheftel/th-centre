from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from ..models import News

__all__ = [
    'NewsAdmin'
]


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)

