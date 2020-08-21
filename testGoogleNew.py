from GoogleNews import GoogleNews

class NewsArticles():
    
    def news(country):
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

v = NewsArticles.news('China')
for a in v:
    print(a)
