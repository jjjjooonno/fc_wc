import requests



### requests 연습문제 1 GET
url = "https://openapi.naver.com/v1/search/blog"
query = '어벤져스'
display = 10
start = 10
sort = 'date'
client_id = "yQnvv5nmW3s99Fm2pGB3"
client_secret = "Any5dmL6Az"
header = {"X-Naver-Client-Id" : client_id, "X-Naver-Client-Secret" : client_secret}
r = requests.get(url+'?query='+query+'&display='+str(display)+'&start='+str(start)+'&sort='+sort,headers = header)
###

rcod = r.status_code
if(rcod==200):
    print(r.text)
else:
    print("Error Code:" + str(rcod))
# 검색어는 어벤져스 / 검색 결과 출력 건수는 10 / 검색 시작위치는 10 / 정렬은 날짜순으로 합니다.