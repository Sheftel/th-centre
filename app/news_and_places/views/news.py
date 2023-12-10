from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from ..serializers import NewsDetailSerializer, NewsListSerializer
from ..models import News


class NewsListView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    