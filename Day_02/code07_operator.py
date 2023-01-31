# 연산자
# 할당연산
# 2 = 1 (X)
val = 1
print('--------------------------------------')

# equal 연산
print(1 == 1)
print('--------------------------------------')

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
#소수 나누기 - 나눗셈 소수점 표시
print(1024 / 2)
#정수 나누기 - 나눗셈 소수점 반올림
print(1024 // 2)
print(6 // 3)
# % - 나머지 표시 연산자
print(12 % 3)
# 나머지 3=>0 6=>0 9=>0
# 배수를 찾을 때 많이 쓰는 연산자

# ZeroDivisionError: division by zero
# 컴퓨터는 무한대를 계산 할 수 없음
# print(6 / 0) 
# print(6 // 0)
print('--------------------------------------')

# 승수 표시
print(2 ** 10)  # 2의 10승
print('--------------------------------------')

# 문자열 연산
first = 'Hello'
second = 'World'

print(first + second)   # 문자열이 붙어있어서 답답함
print(first + ' ' + second)
print(first, second)

print(first * 4)

# 더하기 곱하기 말고는 쓸 수 없음
# print(first - second)
# print(first / second)

# 문자열 길이 len()
print(len(first))
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
# 공백도 요소가 될 수 있음
# print(first[5])
# IndexError: string index out of range

print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
# 파이썬에서 인덱스 찾는 특이한 방법
print('--------------------------------------')

# 리스트 자르기 [시작점 : 종점 + 1]
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:19])

print(current[0:4] + '년' + 
      current[5:7] + '월' + 
      current[8:10] +  '일' + 
      current[11:13] + '시' + 
      current[14:16] + '분' + 
      current[17:19] + '초')

print(current[-19:4])
print('--------------------------------------')

# 리스트 연산
# 리스트는 값 수정, 삽입, 삭제 가능
que = [1, 2, 3, 4, 5]
que[0] = 7

# 지금 있는 범위 내에서 작업할 때 쓰는 꺽쇠
print(que)

# IndexError: list assignment index out of range
# que[5] = 10 안됌

que.append(10)
print(que)
# append는 맨 뒤에 갖다 붙임
que.insert(3, 99)
print(que)
# insert는 원하는 자리에 갖다 붙임
que.remove(10)
print(que)
# remove는 원하는 값 삭제

# 튜플은 기능 자체가 없음
# TypeError: 'tuple' object does not support item assignment
tup = (1, 2, 3, 4, 5)
# tup[1] = 9
print(tup)
print('--------------------------------------')

# 문자열 == 문자 리스트
title = 'python'
print(title[0])
# TypeError: 'str' object does not support item assignment
# title[0]= 'p'
# 문자열에서는 값 변경 x
print('P' + title[1:])

# 일반적인 문자형 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'P'
print(text)
print('--------------------------------------')

# 문자열 포맷팅 - 문자열을 내 마음대로 바꿔 쓰는것
# 문자열에서 {}는 연산자 역할
print("I'm so happy {0} you!!, {1}".format(2, 'Hey'))
# 최신식 문자열 포맷팅
# 맨 앞에 f 빠지면 큰일남
preword = 3
sayHello = 'Hey'
print(f"I'm so happy {preword} you!!, {sayHello}")
print('--------------------------------------')

# 주의 사항 - 소수점 표시하는 법
pi = 3.141592
print(f'파이는 {pi}입니다.')
# 소수점 2째 자리까지 자르기
print(f'파이는 {pi:0.2f}입니다.')
print(f'파이는 {pi:10.3f}입니다.')
print('--------------------------------------')

# 문자열 특정 문자 기준으로 자르기
full_name = 'Park Seong Hyeon'
vals = full_name.split()    # 스페이스
print(type(vals))
print(vals)

vals = full_name.split('S') # 지정
print(vals)

# 특정 문자열 바꾸기
print(full_name.replace('Park', 'Ashely'))

# 문자열 공백 제거
hi = '          Hello~ Bye          '
print(hi.lstrip() + '|')    # 왼쪽 공백 삭제, | 파이프
print(hi.rstrip() + '|')    # 오른쪽 공백 삭제
print(hi.strip() + '|')     # 양쪽 공백 삭제

# 문자열에서 값 찾기 index, find - 위치 찾아줌
print(full_name.index('S'))
# print(full_name.index('z')) 
# ValueError: substring not found

print(full_name.find('e'))  
print(full_name.find('z'))  # 결과 값이 마이너스 값이면 찾는 값이 없다는 소리

# count - 찾는 단어의 개수를 알려줌
print(full_name.count('e'))

# 모든 단어를 대문자 또는 소문자로 변경
print(full_name.upper())    # 대문자
print(full_name.lower())    # 소문자

print('--------------------------------------')

# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)