from selenium import webdriver

chromedriver_address = '/Users/joono'
# 수강생님의 컴퓨터에 있는 크롬드라이버 설치 폴더 경로를 입력합니다.
# 윈도우는 폴더에서 복사해서 가져오는 경우 ₩를 /로 바꿔주셔야 합니다.

driver = webdriver.Chrome(chromedriver_address + '/chromedriver')

keyword = '패스트캠퍼스'

web_url = 'https://search.naver.com/search.naver?query='+keyword+'&where=news&ie=utf8&sm=nws_hty'

driver.get(web_url)
driver_source = driver.page_source

print(driver_source)