# 입력 출력

number = int(input('수를 입력하세요 : '))
# int 없이 그냥 곱하면
# number * 5 = str 100이 5번 나옴
print(f'입력한 수 곱하기 5는 {number * 5}입니다.')

print('Life ' 'is ' 'short')
print('Life' ,'is', 'short')

a = [1, 2, 3, 4]
for i in a:
    print(i, end=' ')
