# 값을 돌려주지 않는 return은 생략가능
# 함수 만드는 방법 4가지

# 1. 파라미터 0 리턴 0
# 2. 파라미터 0 리턴 X
# 3. 파라미터 X 리턴 0
# 4. 파라미터 X 리턴 X

def add(x, y):
    result = x + y
    print(result)

def sub(x, y):
    result = x - y
    print(result)

def mul(x , y):
    result = x * y
    print(result)

def div(x , y):
    result = x // y
    print(result)

def hello():
    print('Hello~!!!')

def hello2():
    msg = 'Hello, Hello~!!!'
    return msg

# 함수호출
hello()
print(hello2())
add(1024, 6)
sub(1024, 24)
mul(1024, 5)
div(1024, 8)