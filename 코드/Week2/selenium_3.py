from selenium import webdriver
import time

chromedriver_address = '/Users/joono'
# 수강생님의 컴퓨터에 있는 크롬드라이버 설치 폴더 경로를 입력합니다.
# 윈도우는 폴더에서 복사해서 가져오는 경우 ₩를 /로 바꿔주셔야 합니다.

driver = webdriver.Chrome(chromedriver_address + '/chromedriver')

web_url = 'https://www.facebook.com/'

driver.get(web_url)

byid = driver.find_element_by_id('email')
byid.send_keys('id')
time.sleep(5)

bycn = driver.find_element_by_class_name('inputtext')
bycn.send_keys('cn')
time.sleep(5)

bycs = driver.find_element_by_css_selector('#email')
bycs.send_keys('cs')
time.sleep(5)

driver_source = driver.page_source