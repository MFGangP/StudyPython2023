# 흐름제어

# if 문
name = '명건'

if name == '명건':
   print('진료실에서 담당의사를 만난다.')
elif name == '다원':
   print('주사실로 간다.')
else:
   print('가만히 앉아있는다.')

# for 문
# arr = [1, 2, 3, 4, 5]

# for var in arr:
#    print(f'{var:2.2f}')

arr2 = ('me', 'my', 'friend', 'jane')

for item in arr2:           # arr2 리스트 개수만큼 반복
   print(f'{item:>10}')     # :>10 몰?루

vals = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

num = 0
for item in vals:
   num += 1
   print(f'{num}번 수는 {item} 입니다')