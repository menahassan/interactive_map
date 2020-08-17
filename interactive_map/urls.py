from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^map/', include('map.urls')),
    url(r'^', include('map.urls')),
    url(r'data/', include('data.urls')),
]
