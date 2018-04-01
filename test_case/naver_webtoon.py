import requests
from bs4 import BeautifulSoup
import re


days = ['mon','tue','wed','thu','fri','sat','sun']
day = days[0]

url = 'http://comic.naver.com/webtoon/weekdayList.nhn?week='+day
# = http://comic.naver.com/webtoon/weekdayList.nhn?week=mon

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

print(title_text)