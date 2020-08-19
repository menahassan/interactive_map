from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from data import countriesPop
from data import trafficking
import json

def index(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/index.html", {
    'pop': pop,
    })

def population1980(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1980.html", {
    'pop': pop,
    })

def population1981(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1981.html", {
    'pop': pop,
    })
def population1982(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1982.html", {
    'pop': pop,
    })
def population1983(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1983.html", {
    'pop': pop,
    })
def population1984(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1984.html", {
    'pop': pop,
    })
def population1985(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1985.html", {
    'pop': pop,
    })
def population1986(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1986.html", {
    'pop': pop,
    })
def population1987(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1987.html", {
    'pop': pop,
    })
def population1988(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1988.html", {
    'pop': pop,
    })
def population1989(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1989.html", {
    'pop': pop,
    })
def population1990(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1990.html", {
    'pop': pop,
    })
def population1991(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1991.html", {
    'pop': pop,
    })
def population1992(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1992.html", {
    'pop': pop,
    })
def population1993(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1993.html", {
    'pop': pop,
    })
def population1994(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1994.html", {
    'pop': pop,
    })
def population1995(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1995.html", {
    'pop': pop,
    })
def population1996(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1996.html", {
    'pop': pop,
    })
def population1997(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1997.html", {
    'pop': pop,
    })
def population1998(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1998.html", {
    'pop': pop,
    })
def population1999(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population1999.html", {
    'pop': pop,
    })
def population2000(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2000.html", {
    'pop': pop,
    })
def population2001(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2001.html", {
    'pop': pop,
    })
def population2002(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2002.html", {
    'pop': pop,
    })
def population2003(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2003.html", {
    'pop': pop,
    })
def population2004(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2004.html", {
    'pop': pop,
    })
def population2005(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2005.html", {
    'pop': pop,
    })
def population2006(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2006.html", {
    'pop': pop,
    })
def population2007(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2007.html", {
    'pop': pop,
    })
def population2008(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2008.html", {
    'pop': pop,
    })
def population2009(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2009.html", {
    'pop': pop,
    })
def population2010(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2010.html", {
    'pop': pop,
    })
def population2011(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2011.html", {
    'pop': pop,
    })
def population2012(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2012.html", {
    'pop': pop,
    })
def population2013(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2013.html", {
    'pop': pop,
    })
def population2014(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2014.html", {
    'pop': pop,
    })
def population2015(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2015.html", {
    'pop': pop,
    })
def population2016(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2016.html", {
    'pop': pop,
    })
def population2017(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2017.html", {
    'pop': pop,
    })
def population2018(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/population2018.html", {
    'pop': pop,
    })

def demo(request):
    pop = json.dumps(countriesPop)
    return render(request, "data/demo.html", {
    'pop': pop,
    })

def human_trafficking(request):
    hTrafficking = json.dumps(trafficking)
    return render(request, "data/human_trafficking.html", {
    'hTrafficking': hTrafficking,
    })


