# 복합형

# 리스트 == 배열 (수정, 추가 가능), 0부터 시작 n-1번 까지
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
print('arr1의 2번 인덱스 값 = ' + str(arr1[2]))

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
print('--------------------------------------')

# 딕셔너리 - 순서가 없음(중괄호)
# 사용자가 제일 싫어하는게 횡 스크롤
# 오른쪽 위에 조그마한 PIP = 미니맵
spiderman = {'name' : 'Peter Parker', 
              'age' : '18', 
           'weapon' : 'Web Shooter',
         'deserter' : '탈영병' }
# 컨트롤 + space 컨텐츠 어시스턴트 단축키
print(spiderman)
print(spiderman['weapon'])
print(spiderman['deserter'])
print(type(spiderman))
print('--------------------------------------')

# 집합 - 순서가 없음(중괄호)
# 중복된 값은 묶어버림
set1 = set([1, 2, 3, 4])
print(set1)

set1 = set('Hello World')
print(set1)