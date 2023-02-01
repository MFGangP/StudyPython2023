# 함수
# 함수정의 - 이건 실행이 아님

# 함수 완벽하게 이해를 하려면 디버깅 해야된다.
# 디버깅 할 때 함수가 있으면 F10을 누르면 안됌.
# 함수 안으로 들어가야 하기 때문에 F11을 눌려서 디버깅 해야함.

def add(x, y):
    result = x + y
    return result

def sub(x, y):
    result = x - y
    return result

def mul(x , y):
    result = x * y
    return result

def div(x , y):
    result = x // y
    return result

# 함수호출
val = add(1024, 6)
print(val)

val = sub(1024, 24)
print(val)

val = mul(1024, 5)
print(val)

val = div(1024, 8)
print(val)