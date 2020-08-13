from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import views
from . import news

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^ajax/get_news/$', news.get_news, name='get_news'),
    path('hdiMap', views.hdiMap, name='hdiMap'),
]

urlpatterns += staticfiles_urlpatterns()
