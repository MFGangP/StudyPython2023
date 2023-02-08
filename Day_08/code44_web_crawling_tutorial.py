# %% [markdown]
# ## 웹 크롤링 
# 
# ### 인터넷 접속 라이브러리 추가
# 
# 

# %%
from urllib.request import urlopen, Request

# 도시별 날씨 검색함수
def get_weather(city):
    # 기상청 홈페이지 도시별 날씨 페이지
    url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
    page = urlopen(url=url)
    # 인코딩은 utf-8로 되어있다.
    text = page.read().decode('utf-8')
    # 텍스트를 찾는데 꺽쇠 뒤에 city를 찾아라
    text = text[text.find(f'>{city}</a'):]
    
    # 기온 가져오기
    for i in range(7):
        # 반복하면서 <tb>에 둘러쌓인 원하는 값 찾기
        text = text[text.find(f'<td>')+1:]
    # 찾은 지점부터 3번 째 값
    start = 3
    # 사이값 찾은 뒤에 있는 </tb>값
    end = text.find('</td>')
    # 시작지점 ~ 종료지점 사이 값
    current_temp = text[start:end]
    print(f'{city}의 현재 기온은 {current_temp}℃ 입니다.')

    # 습도 가져오기
    for i in range(3):
        text = text[text.find(f'<td>')+1:]
    start = 3
    end = text.find('</td>')
    current_humid = text[start:end]
    print(f'{city}의 현재 습도는 {current_humid}％ 입니다.')

if __name__ == '__main__':
    get_weather('부산')