from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token
    })
