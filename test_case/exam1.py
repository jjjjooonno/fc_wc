from selenium import webdriver
from bs4 import BeautifulSoup
keyword = '패스트캠퍼스'
url ='https://www.google.co.kr/search?q='+keyword+'&oq='+keyword+'&aqs=chrome..69i57j69i61l3j69i59l2.2048j0j1&sourceid=chrome&ie=UTF-8'

dr = webdriver.Chrome('/Users/joono/chromedriver')

dr.get(url)

dr_html = dr.page_source

soup = BeautifulSoup(dr_html,'html.parser')

rel_words = soup.find_all('p', attrs = {'class' : 'nVcaUb'})

rel_words_text = []

for word in rel_words:
    rel_words_text.append(word.text)

print(rel_words_text)