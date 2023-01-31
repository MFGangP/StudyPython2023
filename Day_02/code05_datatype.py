# 자료형

# None - 값이 없는 값
None # 컴퓨터 왈 나 몰라
print(None)
type(None)
print(0 == None)
print('' == None)
print('-------------------------------')

# 숫자형

val = 3
print(val)
print(type(val))

val = 3.14
print(val)
print(type(val))

val = 'Hello'
print(val)
print(type(val))

val = 0b1010
print(val)
print(type(val))

val = 0x56
print(val)
print(type(val))

val = 12.1354130958093185908710978590285098190578290
print(val)
print(type(val))

val = 4_520_000 # 사람이 읽기 쉽도록 도와주는 기능
print(val)
print(type(val))

val = 3_099.99
print(val)
print(type(val))

print('-------------------------------')

# 문자열 형

val = 'Life is short, You need Python.'
print(val)
print(type(val))

val = 'Hello\nWorld!'  # \n 탈출문자
print(val)
val = 'Hello\tWorld!'  # \t 탭 - 스페이스 4자리
print(val)
val = 'Hello\t\bWorld!'  # \b 백스페이스
print(val)

val = '''Life is short, 
You need Python.''' # '(홑따옴표) 세개를 쓰면 묶어서 쓸 수 있음
print(val)
# "" 쓰는건 에너지 낭비
val = "Hello World!"
val = 'Hello World!'
# 쌍따옴표 쓸 때 장점
val = "Hi, I'm 'Hugo'"
print(val)
val = 'Hi, I\'m \'Hugo\''
print(val)

print('-------------------------------')

# 불린형 or 불형
참 = True
거짓 = False

print(type(참))
print(type(거짓))

print(1 + 1 == 1)
print(1 + 1 == 2)

# 거짓이라는 False 값 변수가 참이냐고 물어봄
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(2)) # 2 == True 웬만하면 1 이외 값은 쓰지않는다.