import time
import urllib.request, json
from selenium import webdriver

webdriver_path = '/Users/joono/chromedriver'

dr = webdriver.Chrome(webdriver_path)

dr.get("https://www.facebook.com")

id_input = dr.find_element_by_id('email')
id_input.send_keys('페이스북 아이디')
pw_input = dr.find_element_by_id('pass')
pw_input.send_keys('페이스북 비밀번호')

submit_button = dr.find_element_by_id('u_0_2')
submit_button.submit()