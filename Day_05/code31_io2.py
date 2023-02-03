# # 다중입력
# x, y = input('두 영단어를 입력해주세요 : ').split(',')
# print(x.rstrip())
# print(y.lstrip())


# 완전 다중입력(개수가 몇 개든지 상관없음)
inputs = list(map(str, input('단어 입력 : ').split()))
# 들어오는 값을 지정해준 값을 기준으로 쭉 나열해준다.

print(inputs)

inputs = list(map(int, input('정수 입력 : ').split()))
print(inputs)