from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from . import views
from . import news
app_name = "map"
urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
