from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import CountriesForm

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class NewsArticles():
    
    def news():
        articles = []

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')

        driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        
        driver.get('https://www.cnn.com/search?q=US%20England%20embassy&size=10&category=world&type=article')

        try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME , "cnn-search__result-publish-date")))
                res = driver.execute_script("return document.getElementsByTagName('html')[0].outerHTML")

                soup = BeautifulSoup(res, 'lxml')
                box = soup.find('div', {'class': 'cnn-search__results-list'})
                all_news = box.find_all('div', {'class': 'cnn-search__result cnn-search__result--article'})
                
                for new in all_news:
                        contents = new.find('div', {'class': 'cnn-search__result-contents'})
                        headline = contents.find('h3', {'class': 'cnn-search__result-headline'})
                        link = headline.find('a', href=True)['href']
                        title = headline.find('a').text.replace('\n', '')
                        
                        date = contents.find('div', {'class': 'cnn-search__result-publish-date'})
                        t1 = date.find_all('span')[1].text.replace('\n', '')
                        
                        articles = articles + [(title, link, t1)]
        except TimeoutException:
                articles = articles + [("Timeout Exception", "", "")]
        finally:
                driver.quit()

        return articles

# Create your views here.
def index(request):
    list = NewsArticles.news()
    mapbox_access_token = 'pk.my_mapbox_access_token'

    if "country" not in request.session:
        request.session["country"] = ""
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    if request.method == 'POST':
        form = CountriesForm(request.POST)
        if form.is_valid():
            #TODO: make a pin at the location of this country
            request.session["country"] = form.cleaned_data["country"]
            return HttpResponseRedirect('/')
    else:
        form = CountriesForm()
    return render(request, "map/index.html", {
    'mapbox_access_token': mapbox_access_token,
    'form': form,
    'country' : request.session["country"],
    "articles": list,
    })
