from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from map import a
from map import DICT
from map import translated
from map import countriesHDI
from GoogleNews import GoogleNews
import json



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
    articles = NewsArticles('England')
    lst = articles.news()
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
    #'country' : request.session["country"],
    "articles": lst,
    })
