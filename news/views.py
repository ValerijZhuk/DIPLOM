import json

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News
from news.serializers import NewsSerializer
import feedparser


class NewsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        news_data = request.data
        news = News.objects.create(**news_data)
        serialized_news = NewsSerializer(news).data
        return Response(serialized_news)

    def get(self, request):
        news = News.objects.all()
        serialized_news = NewsSerializer(news, many=True).data
        return Response(serialized_news)

    def delete(self, request, pk):
        News.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)


class RSSNewsView(APIView):
    def get(self, request):
        rss_names = ["Title", "Description", "Link"]
        rss_titles = []
        rss_descriptions = []
        rss_links = []
        NewsFeed = feedparser.parse("https://www.championat.com/rss/news/football/england/")
        for i in range(len(NewsFeed.entries)):
            entry = NewsFeed.entries[i]
            rss_titles.append(entry.title)
            rss_descriptions.append(entry.description)
            rss_links.append(entry.link)
        rss_list = []
        for i in range(len(rss_titles)):
            dict1 = {rss_names[0]: rss_titles[i], rss_names[1]: rss_descriptions[i], rss_names[2]: rss_links[i]}
            rss_list.append(dict1)
        rss_json = json.dumps(rss_list)
        return Response(rss_list)
