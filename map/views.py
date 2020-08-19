from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import embassies_consulates
from . import nodiplpresencelist
from . import airpollution
from . import issues_summaries
import json
from map import translated
from GoogleNews import GoogleNews

class NewsArticles():
        def __init__(self, country):
            self.country = country

        def news(self):
            articles = []
            googlenews = GoogleNews(lang='en')
            googlenews.search('USA ' +  self.country + " embassy")
            lst = googlenews.result()

            for i in range(3):
                title = lst[i]['title']
                date = lst[i]['date']
                link = lst[i]['link']
                articles = articles + [(title, link, date)]
            
            return articles

#btw, no more need for dict
# Create your views here.
def index(request):
    #TO DO: automize this
    issue_dict = {"air_polution": ["Bangladesh", "Pakistan", "Mongolia", "Afghanistan", "India", "Indonesia", "Bahrain"],}

    mapbox_access_token = 'pk.my_mapbox_access_token'
    lang_list = json.dumps(translated)

    nodiplpresencecountries = []
    for row in nodiplpresencelist:
        nodiplpresencecountries.append(row[0])

    diplpresencecountries = []
    for row in embassies_consulates:
        diplpresencecountries.append(row[2])

    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token,
    'lang_list' : lang_list,
    'countries' : sorted(list(set(diplpresencecountries + nodiplpresencecountries))),
    'embassy_list': json.dumps(embassies_consulates),
    'issues_summaries' : json.dumps(issues_summaries),
    'nodiplpresencelist': nodiplpresencelist,
    'airpollution': airpollution,
    })
