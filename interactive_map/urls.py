from django.contrib import admin
from django.urls import include, path, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', include('map.urls')),
    path('', include('map.urls')),
    url(r'data/', include('data.urls', namespace='data')),
]
