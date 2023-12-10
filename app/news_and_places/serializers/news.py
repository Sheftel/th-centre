from rest_framework.serializers import ModelSerializer
from ..models import News


__all__ = [
    'NewsDetailSerializer',
    'NewsListSerializer'
]


class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ('author', 'image_preview')


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ('image_preview', )
        ordering = ['-created_at']

