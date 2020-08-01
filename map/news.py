from GoogleNews import GoogleNews
from django.http import JsonResponse

def get_news(request):
    country = request.GET.get('country', None)
    data = {
        'article_list': get_article_list(country)
    }
    return JsonResponse(data)

def get_article_list(country):
    return ["title", "media", "link"] #PLACEHOLDER B/C GOOGLENEWS.RESULT() RETURNS EMPTY LIST
    articles = []
    googlenews = GoogleNews(lang='en')
    googlenews.search('USA ' +  country + " embassy")
    lst = googlenews.result()

    for i in range(3):
        title = lst[i]['title']
        date = lst[i]['date']
        link = lst[i]['link']
        articles = articles + [(title, link, date)]

    return articles
