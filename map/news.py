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
    articles = []
    googlenews = GoogleNews(lang='en')
    googlenews.search(f"US {country} relations")
    lst = googlenews.result()

    for i in range(10):
        title = lst[i]['title']
        media = lst[i]['media']
        date = lst[i]['date']
        link = lst[i]['link']
        desc = lst[i]['desc']
        if country in title or country in desc:
            articles = articles + [[title, media, date, desc]]
        if len(articles) == 2:
            break
    return articles

def get_article_list_issue(country, issue):
    articles = []
    googlenews = GoogleNews(lang='en')
    googlenews.search(f"{country} {issue}")
    lst = googlenews.result()

    for i in range(10):
        title = lst[i]['title']
        desc = lst[i]['desc']
        #to weed out irrelevant articles
        if country in title or issue.lower() in title.lower() or country in desc:
            articles = articles + [[title, lst[i]['media'], st[i]['date'], desc]]
        if len(articles) == 2:
            break
    return articles