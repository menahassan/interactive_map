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
        #options.add_argument('--ignore-certificate-errors')
        #options.add_argument('--ignore-ssl-errors')
        options.add_argument('--headless')
        

        driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        #driver = webdriver.Chrome('chromedriver.exe')      
        
        driver.get('https://www.cnn.com/search?q=US%20England%20embassy&size=10&category=world&type=article')
#        res = requests.get('https://www.cnn.com/search?q=US%20China%20embassy&size=10&category=world')
#        res = driver.execute_script('return document.documentElement.outerHTML')
        
#        driver.find_element_by_class_name("cnn-search__results-list")
#        res = driver.execute_script("return document.getElementsByTagName('div')[0].outerHTML")
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

a = NewsArticles.news()
for l in a:
        print(l)
print(len(a))


