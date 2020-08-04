from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', include('map.urls')),
    path('', include('map.urls')),
    path('data/', include('data.urls')),
]
