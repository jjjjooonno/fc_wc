from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
keyword = '패스트캠퍼스'
url ='https://www.google.co.kr/search?q='+keyword

conn = pymysql.connect(host='localhost', user='root', password='ehdtn0909',
                       db='fc', charset='utf8')

dr = webdriver.Chrome('/Users/joono/chromedriver')

dr.get(url)

dr_html = dr.page_source

soup = BeautifulSoup(dr_html,'html.parser')

rel_words = soup.find_all('p', attrs = {'class' : 'nVcaUb'})

rel_words_text = []

for word in rel_words:
    rel_words_text.append(word.text)

print(rel_words_text)


curs = conn.cursor()
curs.execute("set names utf8")

for word in rel_words_text:
    sql = "INSERT INTO relword VALUES (%s);"
    curs.execute(sql,word)
conn.commit()
conn.close()
dr.quit()