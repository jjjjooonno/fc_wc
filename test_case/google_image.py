from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.parse
from selenium.common.exceptions import ElementNotVisibleException
import time
keyword = urllib.parse.quote('보노보노')
driverpath = '/Users/joono/chromedriver'
url = 'https://www.google.co.kr/search?q='+keyword+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwij-92R8LbXAhWCv7wKHbE7BBoQ_AUICigB&biw=1436&bih=780'

dr = webdriver.Chrome(driverpath)
dr.get(url)
q = True
while q ==True:
    newHeight = dr.execute_script("return document.body.scrollHeight")
    dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    try:
        dr.find_element_by_xpath('//*[@id="smb"]').click()
    except ElementNotVisibleException:
        dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    if newHeight == dr.execute_script("return document.body.scrollHeight"):
        q = False
drt = dr.page_source

soup = BeautifulSoup(drt,'html.parser')
images = soup.find_all('img',attrs = {'class':'rg_ic rg_i'})
print(images)
srcs = []
for image in images:
    parse1 = str(image).split('src=\"')
    parse2 = parse1[1].split('\" ')
    srcs.append(parse2[0])
print(srcs[40])
print(len(srcs))
dr.quit()