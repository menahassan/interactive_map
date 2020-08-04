from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from map import a
from map import DICT
import json
from map import translated

#btw, no more need for dict
# Create your views here.
def index(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    embassy_list = json.dumps(a)
    dictionary = json.dumps(DICT)
    lang_list = json.dumps(translated)
    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token,
    'countries' : sorted(DICT.keys()),
    'embassy_list': embassy_list,
    'dict' : dictionary,
    'lang_list' : lang_list,
    })
