from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from .forms import CountriesForm
from map import DICT
import json

# Create your views here.
def index(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    dictionary = json.dumps(DICT)

    #if "country" not in request.session:
    #    request.session["country"] = ""
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    #if request.method == 'POST':
    #    form = CountriesForm(request.POST)
    #    if form.is_valid():
            #TODO: make a pin at the location of this country
    #        request.session["country"] = form.cleaned_data["country"]
    #        return HttpResponseRedirect('/')
    #else:
    #    form = CountriesForm()
    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token,
    'countries' : sorted(DICT.keys()),
    'dict' : dictionary,
    })
