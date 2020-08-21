from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import views
from . import news
app_name = "map"
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^ajax/get_news/$', news.get_news, name='get_news'),
    url(r'^ajax/get_news_issue/$', news.get_news_issue, name='get_news_issue'),
]

urlpatterns += staticfiles_urlpatterns()
