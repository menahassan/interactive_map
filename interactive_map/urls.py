from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', include('map.urls')),
    path('', include('map.urls')),
    url(r'^map/', include('map.urls', namespace='map')),
    url(r'data/', include('data.urls', namespace='data')),
]
