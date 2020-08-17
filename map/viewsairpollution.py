from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import DICT
from . import a
from . import nodiplpresencelist
from . import airpollution
import json

#btw, no more need for dict
# Create your views here.
def index(request):
    #TO DO: automize this
    issue_dict = {"air_polution": ["Bangladesh", "Pakistan", "Mongolia", "Afghanistan", "India", "Indonesia", "Bahrain"],}

    mapbox_access_token = 'pk.my_mapbox_access_token'
    embassy_list = json.dumps(a)
    dictionary = json.dumps(DICT)

    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token,
    'countries' : sorted(DICT.keys()),
    'embassy_list': embassy_list,
    'dict' : dictionary,
    'issuedict' : json.dumps(issue_dict),
    'nodiplpresencelist': nodiplpresencelist,
    'airpollution': airpollution,
    })
