import requests



### requests 연습문제 1 GET
url = "https://openapi.naver.com/v1/search/blog"
query =
display =
start =
sort =
client_id = ""
client_secret = ""
header = {}
r = requests.get()
###

rcod = r.status_code
if(rcod==200):
    dc = r.json()
    print(dc)
else:
    print("Error Code:" + str(rcod))
# 검색어는 어벤져스 / 검색 결과 출력 건수는 10 / 검색 시작위치는 10 / 정렬은 날짜순으로 합니다.