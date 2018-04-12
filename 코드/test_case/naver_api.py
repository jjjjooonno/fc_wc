import os
import sys
import urllib
import urllib.request
import requests
from pandas import *
import json
client_id = "X9S83UuJsvBu1zKJsdep"
client_secret = "Vph796WJWB"
url = "https://openapi.naver.com/v1/datalab/search"

body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"배그\",\"keywords\":[\"배틀그라운드\",\"pubg\",\"배그\",\"battleground\",\"카배\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\",\"3\",\"4\"],\"gender\":\"f\"}"
header = {"X-Naver-Client-Id": client_id,"X-Naver-Client-Secret" : client_secret, "Content-Type" : "application/json"}
rg = requests.get('https://www.naver.com')

cookie = rg.headers['Set-Cookie']
print(cookie)
r = requests.post(url, data = body.encode(encoding='utf-8'), headers = header)
print(rg.headers)
rcod = r.status_code
if(rcod==200):
    dc = r.json()
    for i in dc['results'][0]['data']:
        print(i['period'], ' : ', i['ratio'])
else:
    print("Error Code:" + str(rcod))
