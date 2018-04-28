from selenium import webdriver
import time

chromedriver_address = '/Users/joono'
# 수강생님의 컴퓨터에 있는 크롬드라이버 설치 폴더 경로를 입력합니다.
# 윈도우는 폴더에서 복사해서 가져오는 경우 ₩를 /로 바꿔주셔야 합니다.

driver = webdriver.Chrome(chromedriver_address + '/chromedriver')

web_url = 'https://www.facebook.com/'
# 이번에는 페이스북 로그인페이지를 들어가서 아이디 입력칸의 위치를 가져와보는 실습입니다.
driver.get(web_url)
# 페이스북 로그인 페이지의 아이디 입력칸의 HTML코드입니다.
# <input type="email" class="inputtext" name="email" id="email" tabindex="1" data-testid="royal_email">
# 아이디 입력칸 엘리먼트는 input 태그이고, id는 email, class는 inputtext인것을 알 수 있습니다.
byid = driver.find_element_by_id('email')
byid.send_keys('id')
time.sleep(5)

bycn = driver.find_element_by_class_name('inputtext')
bycn.send_keys('cn')
time.sleep(5)

bycs = driver.find_element_by_css_selector('#email')
bycs.send_keys('cs')
time.sleep(5)
# 여러가지 접근 방법을 통해 같은 엘리먼트를 다른 코드로 접근합니다.
# .send_keys는 키보드 입력을 코드를 통해 하는 것인데, 3주차에 좀더 심화학습할 예정입니다!
driver_source = driver.page_source
# 마찬가지로 페이지 소스를 가져와 봅니다.
print(driver_source)