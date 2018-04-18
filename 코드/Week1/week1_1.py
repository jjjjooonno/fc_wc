import requests
from bs4 import BeautifulSoup
import re
from pandas import unique

days = ['mon','tue','wed','thu','fri','sat','sun']
day = days[0]

url = 'http://comic.naver.com/webtoon/weekdayList.nhn?week=wed'+day+'&view=list&order=ViewCount'

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html,'html.parser')
title_pattern = re.compile('^/webtoon/list.nhn\?titleId=')
titles = soup.find_all('a',attrs = {'href' : title_pattern})
title_text = []
for title in titles:
    title_text.append(title.text.strip())
while '전체보기' in title_text: title_text.remove('전체보기')
while '' in title_text: title_text.remove('')
while 'NEW' in title_text: title_text.remove('NEW')

print(unique(title_text))