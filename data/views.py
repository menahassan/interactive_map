from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from data import a
import json

def index(request):
    embassy_list = json.dumps(a)
    return render(request, "data/index.html", {
    'embassy_list': embassy_list,
    })
