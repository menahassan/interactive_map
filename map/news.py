from GoogleNews import GoogleNews
from django.http import JsonResponse

def get_news(request):
    country = request.GET.get('country', None)
    data = {
        'article_list': get_article_list(country)
    }
    return JsonResponse(data)

def get_news_issue(request):
    country = request.GET.get('country', None)
    issue = request.GET.get('issue', None)
    data = {
        'article_list': get_article_list_issue(country, issue)
    }
    return JsonResponse(data)

def get_article_list(country):
    return ["title", "media", "date", "link"] #PLACEHOLDER B/C GOOGLENEWS.RESULT() RETURNS EMPTY LIST
    articles = []
    googlenews = GoogleNews(lang='en')
    googlenews.search(f"USA {country} embassy")
    lst = googlenews.result()

    for i in range(3):
        title = lst[i]['title']
        media = lst[i]['media']
        date = lst[i]['date']
        link = lst[i]['link']
        articles = articles + [(title, media, date, link)]
    return articles

def get_article_list_issue(country, issue):
    return ["title", "media", "date", "link"] 
    articles = []
    googlenews = GoogleNews(lang='en')
    googlenews.search(f"{country} {issue}")
    lst = googlenews.result()

    for i in range(10):
        title = lst[i]['title']
        #to weed out irrelevant articles
        if country in title or issue in title:
            articles = articles + [(title, lst[i]['media'], st[i]['date'], lst[i]['link'])]
        if len(articles) == 2:
            break
    return articles



print(get_article_list('China'))
