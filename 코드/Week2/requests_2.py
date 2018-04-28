import requests

url = "https://openapi.naver.com/v1/datalab/search"
client_id = "X9S83UuJsvBu1zKJsdep"
client_secret = "Vph796WJWB"
# naver api를 사용하기 위해 아이디와 비밀번호를 입력합니다.

body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"배그\",\"keywords\":[\"배틀그라운드\",\"pubg\",\"배그\",\"battleground\",\"카배\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\",\"3\",\"4\"],\"gender\":\"f\"}"
header = {"X-Naver-Client-Id": client_id,"X-Naver-Client-Secret" : client_secret, "Content-Type" : "application/json"}
# POST요청을 보내기 위해 택배상자 안에 넣을 정보를 따로 기입해 놓습니다.

r = requests.post(url, data = body.encode(encoding='utf-8'), headers = header)
# post를 사용해 data라는 변수에 우리가 준비한 택배 내용물을 넣고 요청을 보냅니다.

rcod = r.status_code
if(rcod==200):
    dc = r.json()
    for i in dc['results'][0]['data']:
        print(i['period'], ' : ', i['ratio'])
else:
    print("Error Code:" + str(rcod))
# 위의 네이버 API는 키워드에 대한 검색 비율을 json으로 응답해주는 API입니다. 따라서 응답을 .json()으로 해석하여 뽑아냅니다.