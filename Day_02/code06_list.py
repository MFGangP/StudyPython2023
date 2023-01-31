# 복합형

# 리스트 == 배열 (수정, 추가 가능)
# 리스트 미사용 시
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10

print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)

print('--------------------------------------')
# 리스트 사용 시
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
sum = 0
for i in arr:
    sum += i
print(sum)
print('--------------------------------------')

arr1 = [1, 2, 3]
arr2 = [1.1, 2.2, 3.3]
arr3 = ['Hello', 13, 'World!', True]
print(arr1, arr2, arr3)

print(type(arr3))

arr4 = []   # 빈 리스트
arr5 = list()
print(arr4, arr5)

arr6 = [1, 2, 3, 4, [6, 7, 8, [9, 10, 11]]]
print(arr6)

arr7 = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(arr7)

# 튜플 (수정, 추가 불가능)
tuple1 = (1, 2, 3, 4)

arr5.append('4')
print(arr5)

# tuple1.append(4) 튜플은 변경 불가능
print(tuple1)
print(type(tuple1))

# 딕셔너리

