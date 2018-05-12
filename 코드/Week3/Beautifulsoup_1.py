from selenium import webdriver
from bs4 import BeautifulSoup
import time

webdriver_path = '/Users/joono/chromedriver'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
dr = webdriver.Chrome(webdriver_path,chrome_options=chrome_options)
keyword = '어벤져스'


dr.get("https://www.facebook.com")
id_input = dr.find_element_by_id('email')
id_input.send_keys('01027992663')
pw_input = dr.find_element_by_id('pass')
pw_input.send_keys('ehdtn0*0*')

submit_button = dr.find_element_by_id('u_0_2')
submit_button.submit()

dr.get("https://www.facebook.com/datadesigner2015/")
time.sleep(3)
drpage = dr.page_source

soup = BeautifulSoup(drpage,'html.parser')

posts = soup.find_all('div', attrs = {'class' : '_4-u2 _4-u8'})
for post in posts:
    print(post.text)