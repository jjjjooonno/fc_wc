import requests

url = "https://openapi.naver.com/v1/language/translate"
client_id = "q3Pjcs2b4wWHhvwpob9I"
client_secret = "3I3csB3SIu"
# naver api를 사용하기 위해 아이디와 비밀번호를 입력합니다.

body = "{\"source\":\"ko\",\"target\":\"en\",\"text\":\"안녕하세요\"}"
header = {"X-Naver-Client-Id": client_id,"X-Naver-Client-Secret" : client_secret, "Content-Type" : "application/json"}
# POST요청을 보내기 위해 택배상자 안에 넣을 정보를 따로 기입해 놓습니다.

r = requests.post(url, data = body.encode(encoding='utf-8'), headers = header)
# post를 사용해 data라는 변수에 우리가 준비한 택배 내용물을 넣고 요청을 보냅니다.

rcod = r.status_code
if(rcod==200):
    dc = r.json()
    print(dc['message']['result']['translatedText'])
else:
    print("Error Code:" + str(rcod))
# 위의 네이버 API는 키워드에 대한 검색