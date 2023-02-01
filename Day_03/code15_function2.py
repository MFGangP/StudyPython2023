# 값을 돌려주지 않는 return은 생략가능
def add(x, y):
    result = x + y
    print(result)
    return

def sub(x, y):
    result = x - y
    print(result)
    return

def mul(x , y):
    result = x * y
    print(result)
    return

def div(x , y):
    result = x // y
    print(result)
    return

# 함수호출
add(1024, 6)

sub(1024, 24)

mul(1024, 5)

div(1024, 8)