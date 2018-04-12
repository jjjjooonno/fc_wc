from selenium import webdriver
import pymysql
from bs4 import BeautifulSoup

conn = pymysql.connect(host='localhost', user='root', password='비밀번호',
                       db='fc', charset='utf8')
curs = conn.cursor()
dr = webdriver.Chrome('/Users/joono/chromedriver')

# titles = sp.find_all('span',attrs={'data-role' : 'list-title-text'})
# for title in titles:
#     print(title.text)
urlss = []
titles = []
contents = []
comments = []
pages = 3
for page in range(pages):
    dr.get('https://www.clien.net/service/group/community?&od=T31&po={0}'.format(page))
    drt = dr.page_source
    sp = BeautifulSoup(drt, 'html.parser')
    urls = sp.find_all('a', attrs={'class': 'list_reply reply_symph'})
    for url in urls[1:]:
        url_need = 'https://www.clien.net'+url['href'][:-14]
        urlss.append(url_need)
        dr.get(url_need)
        drt_now = dr.page_source
        sp_now = BeautifulSoup(drt_now,'html.parser')
        title = sp_now.find('h3',attrs= {'class' : 'post_subject'}).text
        titles.append(title)
        content = sp_now.find('div',attrs={'class' : 'post_article fr-view'}).text
        comment = sp_now.find_all('div',attrs={'class' : 'comment_view'})
        comments.append([])
        for one_comment in comment:
            comments[-1].append(one_comment.text.strip())
        contents.append(content)
qdx = 0
curs.execute("set names utf8")
for i in range(0,len(comments)):
    sql = "INSERT INTO cont VALUES (%s, %s, %s, %s);"
    curs.execute(sql,(urlss[i], titles[i], contents[i], i))
    for q in comments[i]:
        sql = "INSERT INTO comm VALUES (%s,%s,%s);"
        curs.execute(sql,(qdx,q,i))
        qdx = qdx + 1

conn.commit()
conn.close()
dr.quit()