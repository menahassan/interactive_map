from django.urls import path
from django.conf.urls import url

from . import views
from . import news

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^ajax/get_news/$', news.get_news, name='get_news'),
    url(r'^ajax/get_news_issue/$', news.get_news_issue, name='get_news_issue'),
]
