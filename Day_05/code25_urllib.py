# urllib 패키지 불러오기

from urllib.request import Request, urlopen
# 생성자로 객체 생성 Ctrl + 클릭으로 주소 확인
req = Request('https://www.naver.com')
res = urlopen(req)
# 200은 http 프로토콜 번호 제대로 수신했다는 뜻
# 404는 제대로 못받았다
print(res.status)