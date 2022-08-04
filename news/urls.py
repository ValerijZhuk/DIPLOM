from django.urls import path

from news.views import NewsView, RSSNewsView

urlpatterns = [
    path('', NewsView.as_view()),
    path('delete/<int:pk>/', NewsView.as_view()),
    path('rss/', RSSNewsView.as_view())
]