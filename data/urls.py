from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "data"
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('population1980', views.population1980, name='population1980'),
    path('population1981', views.population1981, name='population1981'),
    path('population1982', views.population1982, name='population1982'),
    path('population1983', views.population1983, name='population1983'),
    path('population1984', views.population1984, name='population1984'),
    path('population1985', views.population1985, name='population1985'),
    path('population1986', views.population1986, name='population1986'),
    path('population1987', views.population1987, name='population1987'),
    path('population1988', views.population1988, name='population1988'),
    path('population1989', views.population1989, name='population1989'),
    path('population1990', views.population1990, name='population1990'),
    path('population1991', views.population1991, name='population1991'),
    path('population1992', views.population1992, name='population1992'),
    path('population1993', views.population1993, name='population1993'),
    path('population1994', views.population1994, name='population1994'),
    path('population1995', views.population1995, name='population1995'),
    path('population1996', views.population1996, name='population1996'),
    path('population1997', views.population1997, name='population1997'),
    path('population1998', views.population1998, name='population1998'),
    path('population1999', views.population1999, name='population1999'),
    path('population2000', views.population2000, name='population2000'),
    path('population2001', views.population2001, name='population2001'),
    path('population2002', views.population2002, name='population2002'),
    path('population2003', views.population2003, name='population2003'),
    path('population2004', views.population2004, name='population2004'),
    path('population2005', views.population2005, name='population2005'),
    path('population2006', views.population2006, name='population2006'),
    path('population2007', views.population2007, name='population2007'),
    path('population2008', views.population2008, name='population2008'),
    path('population2009', views.population2009, name='population2009'),
    path('population2010', views.population2010, name='population2010'),
    path('population2011', views.population2011, name='population2011'),
    path('population2012', views.population2012, name='population2012'),
    path('population2013', views.population2013, name='population2013'),
    path('population2014', views.population2014, name='population2014'),
    path('population2015', views.population2015, name='population2015'),
    path('population2016', views.population2016, name='population2016'),
    path('population2017', views.population2017, name='population2017'),
    path('population2018', views.population2018, name='population2018'),
    path('demo', views.demo, name='demo'),
    path('human_trafficking', views.human_trafficking, name='human_trafficking')
]

urlpatterns += staticfiles_urlpatterns()