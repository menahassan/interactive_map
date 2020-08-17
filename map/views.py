from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import embassies_consulates
from . import nodiplpresencelist
from . import airpollution
import json

#btw, no more need for dict
# Create your views here.
def index(request):
    #TO DO: automize this
    issue_dict = {"air_polution": ["Bangladesh", "Pakistan", "Mongolia", "Afghanistan", "India", "Indonesia", "Bahrain"],}

    mapbox_access_token = 'pk.my_mapbox_access_token'

    nodiplpresencecountries = []
    for row in nodiplpresencelist:
        nodiplpresencecountries.append(row[0])

    diplpresencecountries = []
    for row in embassies_consulates:
        diplpresencecountries.append(row[2])

    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token,
    'countries' : sorted(list(set(diplpresencecountries + nodiplpresencecountries))),
    'embassy_list': json.dumps(embassies_consulates),
    'issuedict' : json.dumps(issue_dict),
    'nodiplpresencelist': nodiplpresencelist,
    'airpollution': airpollution,
    })

#^i used this to find set of countries not among the list in the original excel w/ embassies
