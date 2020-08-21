from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import embassies_consulates
from . import nodiplpresencelist
from . import airpollution
from . import co2emissions
from . import povertyrate
from . import issues_summaries
from map import a
from map import DICT
import json
from map import translated
from GoogleNews import GoogleNews

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

    issues = []
    for row in issues_summaries:
        issues.append(row[0])

    lang_list = json.dumps(translated)
    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token,
    'countries' : sorted(list(set(diplpresencecountries + nodiplpresencecountries))),
    'embassy_list': json.dumps(embassies_consulates),
    'issues_summaries' : json.dumps(issues_summaries),
    'nodiplpresencelist': nodiplpresencelist,
    'airpollution': airpollution,
    'co2emissions':co2emissions,
    'povertyrate':povertyrate,
    'lang_list' : lang_list,
    'issues':issues,
    })
