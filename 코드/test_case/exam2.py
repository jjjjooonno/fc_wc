from selenium import webdriver
import requests

from bs4 import BeautifulSoup
import pymysql
keyword = '패스트캠퍼스'
url ='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='+keyword

# 1. 셀레늄 웹드라이버 사용

# conn = pymysql.connect(host='localhost', user='root', password='비밀번호',
#                        db='fc', charset='utf8')

# dr = webdriver.Chrome('/Users/joono/chromedriver')

# dr.get(url)

# dr_html = dr.page_source
#
# soup = BeautifulSoup(dr_html,'html.parser')
#
# rel_words = soup.find_all('p', attrs = {'class' : 'nVcaUb'})
#
# rel_words_text = []
#
# for word in rel_words:
#     rel_words_text.append(word.text)
#
# print(rel_words_text)


# curs = conn.cursor()
# curs.execute("set names utf8")
#
# for word in rel_words_text:
#     sql = "INSERT INTO relword VALUES (%s);"
#     curs.execute(sql,word)
# conn.commit()
# conn.close()
# dr.quit()

# 2. requests 사용

dr = requests.get(url)

dr_html = dr.text

soup = BeautifulSoup(dr_html,'html.parser')

rel_words_parent = soup.find('ul', attrs = {'class' : '_related_keyword_ul'})
rel_words_chil = rel_words_parent.findChildren()
rel_words_text = []

print(dr_html)

for word in rel_words_chil:
    rel_words_text.append(word.text)

print(rel_words_text)