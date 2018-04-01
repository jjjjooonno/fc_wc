from browsermobproxy import Server
import time
import urllib.request, json
from pandas import *
from selenium import webdriver
import datetime

date = datetime.datetime.now()
nowdate = date.strftime('%Y%m%d')
server = Server("/Users/joono/browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

webdriver_path = '/Users/joono/chromedriver'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server={host}:{port}'.format(host='localhost', port=proxy.port))

dr = webdriver.Chrome(webdriver_path,chrome_options=chrome_options)
proxy.new_har("kakao", options={'captureHeaders': True, 'captureContent': True})

dr.get("https://e.kakao.com/t/friends-blossom")
dr.refresh()

time.sleep(1)

url_json_holder = []
for ent in proxy.har['log']['entries']:
    url_json = str(ent['request']['url'])
    print(url_json)