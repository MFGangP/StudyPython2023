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

## 자습

내일 1교시를 들을 수 없는 상황이라 혼자 자료보고 if문 for 문 자습함

```Python
        arr2 = ('me', 'my', 'friend', 'jane')

        for item in arr2:           # arr2 리스트 개수만큼 반복
        print(f'{item:>10}')     # :>10 몰?루
```
예문에 문자열 포맷팅 최신 버전을 처음봐서 처음보는 방식이라 무슨 소리인지 모르겠네....

>':' 뒤에 정수를 전달하면 해당 필드의 최소 문자 폭이 됩니다. 열을 줄 맞춤할 때 편리합니다. 
>
>[7. 입력과 출력] <https://docs.python.org/ko/3/tutorial/inputoutput.html>

최소 문자 폭을 10 이상으로 지정 하는건가? 내일 강사님한테 제대로 물어봐야겠다.

### 2023.02.01

문자폭을 10 글자로 지정 한 다음 오른쪽 정렬 한다는 뜻

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 디버깅
        - Ctrl + F5(디버깅 없이 실행), F5(디버깅), F9(해당 줄 디버깅), F10(한 줄 씩 실행), F11
    - 함수
        - 전역/지역함수
        - 람다함수 

>함수 이름 선택 = 더블클릭

>동일한 함수 이름 전체 변경 = F2

>동일한 함수로 자리이동 = F7

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