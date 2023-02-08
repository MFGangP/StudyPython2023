# studypython2023
부경대 IoT 파이썬 학습 리포지토리

## 1일차

1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치
>
2. 파이썬 기본
    - console 출력
    - 주석

```python
# date : 2023-01-30 - 주석
# author : Parkseonghyeon
# desc : 콘솔 출력
# console 출력 / 여기는 주석입니다! 
# 주석 열심히 달기
print('Hello, Python!!') # 콘솔출력 함수
```

## 2일차

1. 파이썬 기본

    - 변수
    - 자료형
    - 연산자

```python
# 변수
val = 1

# 자료형
print(type(val))    # <class 'int'>

# 문자열 포맷팅 - 문자열을 내 마음대로 바꿔 쓰는것
# 문자열에서 {}는 연산자 역할
print("I'm so happy {0} you!!, {1}".format(2, 'Hey'))

# 최신식 문자열 포맷팅
# 맨 앞에 f 빠지면 큰일남
preword = 3
sayHello = 'Hey'
print(f"I'm so happy {preword} you!!, {sayHello}")

# 주의 사항 - 소수점 표시하는 법
pi = 3.141592
print(f'파이는 {pi}입니다.')        # 파이는 3.141592 입니다.
# 소수점 2째 자리까지 자르기
print(f'파이는 {pi:0.2f}입니다.')   # 파이는 3.14 입니다.
print(f'파이는 {pi:10.3f}입니다.')  # 파이는          3.142 입니다.
```

### 자습

    내일 1교시를 들을 수 없는 상황이라 혼자 자료보고 if문 for 문 자습함

```Python
arr2 = ('me', 'my', 'friend', 'jane')

for item in arr2:           # arr2 리스트 개수만큼 반복
print(f'{item:>10}')     # :>10 몰?루
```
    예문에 문자열 포맷팅 최신 버전을 처음봐서 처음보는 방식이라 무슨 소리인지 모르겠네....

> ':' 뒤에 정수를 전달하면 해당 필드의 최소 문자 폭이 됩니다. 열을 줄 맞춤할 때 편리합니다. 
> [7. 입력과 출력] <https://docs.python.org/ko/3/tutorial/inputoutput.html>

    최소 문자 폭을 10 이상으로 지정 하는건가? 내일 강사님한테 제대로 물어봐야겠다.

### 2023.02.01

문자 폭을 10 글자로 지정 한 다음 오른쪽 정렬 한다는 뜻

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 디버깅
        - Ctrl + F5(디버깅 없이 실행), F5(디버깅), F9(해당 줄 디버깅), F10(한 줄 씩 실행), F11(한 줄 씩 자세하게 디버깅)
    - 함수
        - 전역/지역함수
        - 람다함수 <br/><br/>
    >함수 이름 선택 = 더블클릭
    >
    >동일한 함수 이름 전체 변경 = F2
    >
    >동일한 함수로 자리이동 = F7
    >
    >ctrl + k + c 주석처리
    >
    >디버깅 끝내기 = Shift + F5

### 복습

    지역/전역변수는 이미 아는 부분이라 괜찮았고, 별 증가 시키는 2줄 짜리 코딩을 쓸데없이 혼자 꼬아서 어렵게 생각했다. 2중 for 문인줄 알았더니;

    혼자 함수 만들면서 리스트 써본적은 없어서 가져온 예문, 이렇게도 만들 수 있다.

```python
def calc(option, *args):
    result = 0

    if option == 'add':
        for i in args:
            result += i
    
    elif option == 'mul':
        result = 1
        for i in args:
            result *= i

    elif option == 'sub':
        result = args[0]
        for i in args[1:]:
            result -= i

    elif option == 'div':       
        result = args[0]
        for i in args[1:]:
            result /= i
```
    오늘은 단축키 알아낸거 만으로도 충분히 편해졌다.

## 4일차
1. 파이썬 기본
    - 가상환경
    - 객체지향 OOP
        - 클래스(상속 전까지)
    - 패키지

    ### Virtualenv 가상환경<br/><br/>
    pip는 개발자인데 모르면 죽음. 라즈베리파이 할 때 맨날 쓰던 그것<br/><br/>
    버전이 다른 개발툴로 기존에 사용하던 코드 실행하면 충돌이 일어나서 안될 때가 있음. 그럴 때 가상환경 구축해놓고 넘어가면서 사용함. (앱플레이어 생각하면 이해하기 쉬움)<br/><br/>
    pip, dir, cd, .\, .(자기자신), ..(부모폴더),  

    ### 객체지향, 클래스

    - 객체지향이 뭐냐?
        - 절차지향 <-> 객체지향
        - 명사, 동사
        - 현실의 모든 것을 컴퓨터 안으로 집어넣는 것을 목표로 만들어진 언어들 - 객체지향
        - 모든 객체는 변수(동사)와 함수(명사)의 집합
        - 명사 = 변수
        - 동사 = 함수 + (옵션 - 파라미터)
        - 변수 없는 함수, 함수 없는 >변수 다 가능
        - 붕어빵 = 객체
        - 붕어빵 틀 = 클래스
        - 클래스 = 객체를 만들기 위해 만들어놓은 틀
        - 변수를 클래스 안에서 쓰면 속성(변수)라고 부름 = 맴버 변수
        - 클래스 안에서 함수는 맴버 함수 - self 필수
        - 사용할 때는 self 빼고 쓴다.
        - 클래스를 사용해서 만든 객체를 인스턴스(실체)라고 함
        - 클래스를 만들 때는 소괄호를 안쓰지만 호출할 때는 소괄호를 씀, 객체를 만들어라(생성)<br/><br/>

    ### 매직 메서드

    기존에 만들어져 있던 매직 메서드를 다시 정의해서 자기 자신한테 맞게 설정하는 것 = 재정의(오버라이딩)

        - new는 새로운 클래스를 만듦 = 얘가 진짜 생성자(잘 안씀)
        - init은 초기화 할 때 새로운 변수 값 할당(근데 얘를 생성자라 부름)
        - 부모, 자식 클래스
        - 상속 = 모든 기능을 다 사용할 수 있음

    ### 패키지, 모듈, 라이브러리

        - 모듈
            - 코드를 포함 하고있는 파일 자체 - 중괄호 {} 표시
            - import를 통해 불러옴
        - 패키지 = 라이브러리
            - 모듈을 여러개 묶어서 큰 단위로 만든 것

```python
import math as m
# 모듈 이름 원하는 대로 바꾸기
# 클래스로 안되어 있는 모듈도 있음
```
    개념은 이해했는데 디버깅하면서 다시 생각해봐야 하는 코드
    뭔가 눈에 확 안들어와서 햇갈림

```python
class Car:

    __number = '54라 9538'
    # __ 이 변수에 직접적으로 접근하지말라.

    def get_number(self) -> str:
        return self.__number

    # 클래스 외부에선 변경 X, 멤버 함수로는 내부를 조작 O
    def set_number(self, number):
        self.__number = number

    def __init__(self, number = '54라 9538') -> None:
        print('__init__')
        self.__number = number
        
    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls) # 부모 클래스 (상속)

    # 부모 클래스 생성자를 생성해서 new를 실행해라
    # new는 새로운 클래스를 만듦 - 얘가 진짜 생성자(잘 안씀)
    # init은 초기화 할 때 새로운 변수 값 할당 - 근데 얘가 생성자라 부름

    def __str__(self) -> str:
        return f'제 차 번호는 {self.__number}입니다. ' 

yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number = '54라 9999'  # 외부에서는 멤버변수에 접근 불가
print(yourcar)
print('클래스 내부 함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제 차는 아이오닉이고, 번호는 {mycar.get_number()}입니다.')

mycar.__number = '132거 8874'
print(mycar.get_number())
print(mycar)

# 외부(객체)에서 클래스 내부의 속성값을 못바꾸게 하는 것
# 캡슐화
# 개발자의 권한을 못 건드리게 만드는것
```
    하나씩 풀어서 보면 무슨 말인지 알겠는데 큰 덩어리로 보니까 이해가 안됐다. 다시 보니까 이해 됌

## 5일차

1. 파이썬 기본
    - 패키지 계속
    - 입출력 다시
    - 예외처리
    - 객체지향 다시<br>
- 패키지 - 모듈
    - 패키지랑 이름 겹치게 파일 이름 지으면 안됌.
    - 라이브러리 -> 모듈 -> 클래스, 함수 등등
    - 외부 패키지 사용 - pip install requests
    - 설치하고 한번 껏다켜야 작동
    - 엔트리 포인트 - 프로그램이 시작되는 진입점 실행 되는 애가 메인
    - [if __name__ == '__main__'] = 매직 변수<br>
- 입출력 다시
    - 입출력
    - 파일 입출력
    - r(읽기), w(새로 만들기), a(첨부)
    - 파일 열고 close 안하면 큰일남
    - UTF-8 사용<br>

```PYTHON
file = open('sample.txt','w', encoding='UTF-8')
```
<br>
    - 절대경로, 상대경로 -> 경로를 패스라고 부른다.<br>
    - 절대경로<br>
    - root 드라이브 부터 모든 경로를 다 적는 것<br>
    - 경로 표시 할 때는 [\]를 두개씩 , 버전이 바뀌어서 그런지 한개도 인식을 해주긴한다, (유닉스,리눅스 등등)[/]이거도 사용 가능 이게 공용이라서 이거 쓰는게 좋음, 써줘야 제대로 찾아감<br>
    - 상대경로<br>
    - 지금 들어와있는 폴더에서 부모 또는 형제 폴더로 가는 경로  ex) ..(부모 폴더), .(자기자신)<br>
<br>

```python
file = open('C:\\Source\\studypython2023\\fileiotest\\sample01.txt','w', encoding='UTF-8') # 파일 쓰기로 만듦

file = open('./fileiotest2/../fileiotest/sample02.txt','a', encoding='UTF-8') # 파일 첨부 and 상대 경로 사용

file = open('./fileiotest/sample01.txt', 'r', encoding='utf-8') # 파일 읽기

while True:
    text = file.readline()
            # 한 줄 씩 읽기
    if not text:
        break
    else:
        print(text)

    file.close
```
### 예외처리
- 코딩 도중에 빨간줄
    - 오류 Error =  코딩 중 발생할 수 있는 문법적 실수
- 실행 도중에 나가버림
    - 예외 = Exception은 실행중에 발생할 수 있는 로직적 실수
- 비정상 종료
    - 다른 명령어 실행 안하고 종료되버릴 때
- 조사식 이용할 것

```python
# 오류가 날 것 같은 줄에 try
try:
    print(div(x, y))
except:
    print('나누기 실패 : 0으로 나누려고 했습니다.')
```
- 단 [except Exception as e:]이 상단에 올라오면 안됌 제일 아래에 존재해야한다.
- 예외 여러 개 할 필요 없다 다 잡아준다.(사용자가 요청하면 바꿔라) 
- 대신 예외는 안나야한다. 

## 6일차

1. 파이썬 기본
    - 콘솔출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중 상속

2. 파이썬 응용
    - 주소록 프로그램 만들기 [소스](https://github.com/MFGangP/StudyPython2023/blob/main/Project/address_app.py)

실행화면
![실행화면](https://github.com/MFGangP/StudyPython2023/blob/main/Images/address_app.png?raw=true)

출력화면
![출력화면](https://github.com/MFGangP/StudyPython2023/blob/main/Images/address_app2.png?raw=true)

3. 주피터 노트북 조금


## 7일차

1. 파이썬 응용
    - 주피터 노트북
        - 사용법
            - 노트북 생성 : 파일메뉴 -> 새파일
            - Ctrl +  Alt + Window + N -> 주피터 파일 생성
        - 단축키
        - 디버깅
            - 설정 ->Debug: Allow 체크
            - 환경에 따라 디버깅이 안될 때가 있다. 그럴 경우 파이썬 파일로 내보내기 한 다음 디버깅 하면 정상 작동한다.<br>
    - 리스트 연산 추가<br>
    - json = 딕셔너리로 표현, 파일 크기가 작아서 전송하기 좋다.<br>
    - json read / write (dump, ensure_ascii, indent)<br>
    - 라이브러리 사용법
        - folium (지도 라이브러리)
        - ex)! pip install pandas
<br>

오늘은 다른 사람들이 만들어놓은 라이브러리 사용이라 딱히 어려운건 없어서 쉬웠다.<br> 대신 사용할 수 있는 범위가 넓어서 알아두면 두고두고 쓰일 것 같다

```python
fileName = './skorea-provinces-2018-geo.json'
m = folium.Map(location=[37.566345, 126.977893],
               zoom_start=7,
               zoom_control=True)
gfile = open(fileName, 'r', encoding='utf-8').read()
jsonData = json.loads(gfile) # json 파일 텍스트를 전부 읽어옴
folium.GeoJson(jsonData, name='대한민국 지역경계').add_to(m)
m
```

## 8일차

1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹크롤링
        - 기상청 오늘의 날씨 크롤링
        - 데이터 포털 OpenAPI 크롤링
        - BeautifulSoup 크롤링
    
![실행화면](https://github.com/MFGangP/StudyPython2023/blob/main/Images/jupiter_folium_openapi_crawling.png?raw=true)<br>
Folium OpenAPI 연동 화면

## 9일차
1. 파이썬 응용

    - 윈폼 개발(GUI)
        - GUI 개발(PyQt)
    - 자료구조 추가
    - 응용 학습

