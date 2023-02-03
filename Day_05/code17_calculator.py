# 좀 더 복잡한 계산기

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

    return result

# print(calc('add', 5, 7, 17))    # 29
# print(calc('mul', 512, 2, 2, 2, 2))    # 2048
# print(calc('sub', 10, 248, 396))    # -634
# print(calc('div', 100, 2))    # 50 
# print(calc('div', 100, 0))    # 제로 디비젼

def new_calc(x,y):
    return (x*y, x/y, x+y, x-y)
# 여러 값을 리턴할 때는
# 결과값은 바뀌면 안되기 때문에 튜플로 처리가 되서 리턴 된다.

# 받을 때는 튜플(소괄호) 생략 가능
res1, res2, res3, res4 = new_calc(5,7)
#(res1, res2, res3, res4) = new_calc(5,7)
# print(res1, res2, res3, res4)