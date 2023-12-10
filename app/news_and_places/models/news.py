import base64
import sys

from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.db.models import Model, CharField, DateTimeField, ImageField, TextField

"""
    Вопросы:
        1. Автор - пользователь, создавший новость или просто строка с фио? - Реализовано как строка, потому что аутентификация пользователей не указана в задании и займет дополнительное время. 

"""


class News(Model):
    title = CharField(max_length=255)
    image = ImageField(upload_to='news/', null=True, max_length=255)
    image_preview = ImageField(upload_to='news/thumbnails/', null=True, max_length=255)

    text = TextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)
    author = CharField(max_length=255)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def save(self, **kwargs):
        if not self.image:
            self.image_preview = None
        else:
            image_data = BytesIO()
            image = Image.open(self.image)
            resize_rate = max(200 / image.width, 200 / image.height)
            preview_size = (image.width*resize_rate, image.height*resize_rate)
            image.thumbnail(preview_size)
            image.save(image_data, 'png')
            self.image_preview = InMemoryUploadedFile(image_data, 'ImageField',
                                                      f"{self.image.name.split('.')[0]}.png",
                                                      'image/jpeg',
                                                      sys.getsizeof(image_data), None)

        super(News, self).save(**kwargs)
