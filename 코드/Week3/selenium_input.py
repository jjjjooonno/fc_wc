import time
import urllib.request, json
from selenium import webdriver

keyword = '혜화역'
webdriver_path = '/Users/joono/chromedriver'


dr = webdriver.Chrome(webdriver_path)

dr.get("https://www.zigbang.com/")

dr.find_element_by_id('room-textfield').send_keys(keyword)
time.sleep(5)
dr.find_element_by_xpath('//*[@id="search_btn"]').click()
time.sleep(10)

des = dr.find_element_by_id('deposit_s')
for option in des.find_elements_by_tag_name('option'):
    if option.text == '100만':
        option.click() # select() in earlier versions of webdriver
        break

dee = dr.find_element_by_id('deposit_e')
for option in dee.find_elements_by_tag_name('option'):
    if option.text == '500만':
        option.click() # select() in earlier versions of webdriver
        break