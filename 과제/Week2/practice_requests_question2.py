import requests

url = "https://openapi.naver.com/v1/language/translate"

### requests 연습문제 2 POST
client_id = ""
client_secret = ""
body = "{}"
header = {}
r = requests.post()
###

rcod = r.status_code
if(rcod==200):
    dc = r.json()
    print(dc['message']['result']['translatedText'])
else:
    print("Error Code:" + str(rcod))
# 해석할 한국어는 안녕하세요 결과 값은 Hello. 가 나오게 코드를 작성해 주세요!