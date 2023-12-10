from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import NewsDetailView, NewsListView

urlpatterns = format_suffix_patterns([
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
])
