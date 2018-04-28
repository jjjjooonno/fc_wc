from selenium import webdriver

chromedriver_address = '/Users/joono'
# 수강생님의 컴퓨터에 있는 크롬드라이버 설치 폴더 경로를 입력합니다.
# 윈도우는 폴더에서 복사해서 가져오는 경우 ₩를 /로 바꿔주셔야 합니다.

driver = webdriver.Chrome(chromedriver_address + '/chromedriver')

keyword = '패스트캠퍼스'
# 이번에는 키워드 검색을 할 수 있는 url이기 때문에 키워드 parameter에 들어갈 키워드를 미리 변수로 지정합니다.
web_url = 'https://search.naver.com/search.naver?query='+keyword+'&where=news&ie=utf8&sm=nws_hty'
# 네이버 뉴스 검색에 키워드를 넣은 주소를 web_url에 저장합니다.
driver.get(web_url)
# 키워드를 넣은 주소에 접근합니다.
driver_source = driver.page_source
# 검색 결과의 HTML문서를 가져옵니다.

print(driver_source)
# HTML 문서를 확인합니다.