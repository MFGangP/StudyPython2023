# 예외처리

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# 입력부터 에러가 나면 종료시켜야된다 진행시키면 안됌
try:
    x, y = input('두 수를 입력하세요 : ').split()
    x = int (x)
    y = int (y)
# except ZeroDivisionError as e:
#     print('0으로 나눌 수 없습니다.')
except Exception as e:
    print(e)    # 이게 실행되고 꺼짐
    exit()
# 단 [except Exception as e:]이 상단에 올라오면 안됌 제일 아래에 존재해야한다.
# 예외 여러 개 할 필요 없다 다 잡아준다.(사용자가 요청하면 바꿔라) 
# 대신 예외는 안나야한다. 
finally:
    print('계속되나?')
# 이거 실행 뒤에 종료됌 - 안될 줄 알았는데 이게 되네(?)


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
# 예외 클래스 사용
except Exception as e:
    print(e)
finally:
    print('계산은 계속됩니다!')
# try문에서 예외가 발생하든 안하든 나옴


print(add(x, y))
print(mul(x, y))