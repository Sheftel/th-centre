from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from ..models import News

__all__ = [
    'NewsAdmin'
]


@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    exclude = ('image_preview',)
    summernote_fields = ('text',)

