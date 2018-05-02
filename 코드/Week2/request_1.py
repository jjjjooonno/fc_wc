import requests
# requests 패키지를 불러옵니다.

response  = requests.get('https://www.naver.com')
# get을 사용해 naver홈페이지 정보를 요청합니다.
# 이때 웹서버의 응답은 response라는 변수에 저장됩니다!

response_code = response.status_code
# 웹서버로부터 도착한 response에 status_code를 사용해
# 요청에 대한 응답이 잘 왔는지 확인합니다.

if response_code == 200:
    print(response.text)
else:
    print('error code : '+str(response_code))
