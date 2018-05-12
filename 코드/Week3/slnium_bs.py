#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common import action_chains
import urllib.request
import time
import sys

dr = webdriver.Chrome('/Users/joono/chromedriver')

dr.implicitly_wait(3)

dr.get('http://store.musinsa.com/app/contents/bestranking?new_product_yn=Y')

dr.find_elements_by_class_name('division_search_input')[0].send_keys(50000)
dr.find_elements_by_class_name('division_search_input')[1].send_keys(100000)
dr.find_element_by_class_name('division_search_btn').click()
dr.find_element_by_xpath('//*[@id="catelist"]/div[2]/dl/dd/ul/li[1]/a')

time.sleep(2)
q = True
target = 1000
while q:
    now_height = dr.execute_script("return window.pageYOffset;")
    dr.execute_script("window.scrollTo(500, {0});".format(target))
    time.sleep(3)
    target = target + 1000
    new_height = dr.execute_script("return window.pageYOffset;")
    if now_height == new_height:
        break
items = dr.find_element_by_id('searchList')
images = items.find_elements_by_css_selector('img[src^="//image.musinsa.com/images"]')
brands = items.find_elements_by_class_name('item_title')
prices = items.find_elements_by_class_name('price')

image_urls = []
brand_l = []
price_l = []
for image in images:
    image_urls.append(image.get_attribute("src"))
for brand in brands:
    brand_l.append(brand.text)
for price in prices:
    price_list = price.text.split('\n')
    if len(price_list) == 3:
        price_l.append(price_list[1])
    else:
        price_l.append(price_list[0])
for index, image_url in enumerate(image_urls):
    urllib.request.urlretrieve(image_url,sys.path[1]+'/실습결과/'+brand_l[index]+price_l[index]+'.'+image_url.split('.')[-1])
