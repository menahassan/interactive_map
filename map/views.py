from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from .forms import CountriesForm
from map import DICT
from map import a
import json

#btw, no more need for dict
# Create your views here.
def index(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    embassy_list = json.dumps(a)
    dictionary = json.dumps(DICT)


    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token,
    'countries' : sorted(DICT.keys()),
    'embassy_list': embassy_list,
    'dict' : dictionary,
    })
