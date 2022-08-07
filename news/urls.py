from django.urls import path

from news.views import NewsView, RSSNewsView, DeleteNews

urlpatterns = [
    path('', NewsView.as_view()),
    path('delete/<int:pk>/', DeleteNews.as_view()),
    path('rss/', RSSNewsView.as_view())
]