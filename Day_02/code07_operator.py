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

