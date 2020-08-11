from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from data import a
from data import DICT
import json

def index(request):
    embassy_list = json.dumps(a)
    mydict = json.dumps(DICT)
    return render(request, "data/index.html", {
    'embassy_list': embassy_list,
    'mydict': mydict,
    })
