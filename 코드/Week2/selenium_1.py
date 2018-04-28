from selenium import webdriver

chromedriver_address = '/Users/joono'
# 수강생님의 컴퓨터에 있는 크롬드라이버 설치 폴더 경로를 입력합니다.
# 윈도우는 폴더에서 복사해서 가져오는 경우 ₩를 /로 바꿔주셔야 합니다.

driver = webdriver.Chrome(chromedriver_address + '/chromedriver')
# 파이썬에서 우리가 설치한 웹드라이버를 인식할 수 있도록 경로를 알려줍니다.

web_url = 'http://news.naver.com/'
# 정보를 요청할 웹페이지의 주소를 미리 web_url에 저장합니다.

driver.get(web_url)
# get방식을 사용하여 정보를 요청합니다. 이때 크롭 브라우저가 열리면서 네이버 홈페이지에 접근합니다.
driver_source = driver.page_source
# 페이지의 소스를 가져옵니다. 이때 HTML문서를 가져오게 됩니다.

print(driver_source)