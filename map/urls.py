from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import views
from . import news
app_name = "map"
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    url(r'^ajax/get_news/$', news.get_news, name='get_news'),
    url(r'^ajax/get_news_issue/$', news.get_news_issue, name='get_news_issue'),
    path('hdiMap', views.hdiMap, name='hdiMap'),
    path('embassyYearOpen', views.embassyYearOpen, name='embassyYearOpen'),
]

urlpatterns += staticfiles_urlpatterns()
