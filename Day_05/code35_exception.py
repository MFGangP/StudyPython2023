# 예외처리

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

x, y = input('두 수를 입력하세요 : ').split()
x = int (x)
y = int (y)

# 가장 원시적인 예외처리 방법
# if y == 0:
#     print('Y에 0을 넣지마세요')
#     exit()
# else:




# Traceback (most recent call last):
#   File "C:\Source\studypython2023\Day_05\code35_exception.py", line 17, in <module>
#     print(div(x, y))
#           ^^^^^^^^^   
# 오류 난 곳
#   File "C:\Source\studypython2023\Day_05\code35_exception.py", line 10, in div
#     return a / b
#            ~~^~~      
# 오류 나는 원인
# ZeroDivisionError: division by zero

print('계산 테스트')
# 오류가 날 것 같은 줄에 try
try:
    print(div(x, y))
except:
    print('나누기 실패 : 0으로 나누려고 했습니다.')

print(add(x, y))
print(mul(x, y))