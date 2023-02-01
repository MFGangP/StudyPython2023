# # for 문

arr = [1, 2, 3, 4, 5]
sum = 0

for item in arr:
   sum = sum + item
   sum += item  # sum = sum + item
print('합계는 ', f'{sum:2.2f}')

arr2 = ('me', 'my', 'friend', 'jane')

for item in arr2:           # arr2 리스트 개수만큼 반복
   print(f'{item:>10}')     # :>10 몰?루

vals = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

num = 0
for item in vals:
   num += 1
   print(f'{num}번 수는 {item} 입니다')

# 
# 리스트를 편하게 만드는 방법 ~ for ~ in range( , )
vals = [i for i in range(1,11)]  
# 0부터 시작하니까 끝자리 원하는 범위 +1 해줘야함
print(vals)

# continue / break
# if 문 안에 쓰는게 아니라 for 문 안에서만 쓰는 것
num = 0
for item in vals:
   num += 1
   if num % 2 == 0:
      # 이후의 것을 수행하지 않고 다시 for 문으로 회귀
      # continue 
      break # break를 만나면 for 문을 완전히 탈출
   elif num % 2 != 0:
      print(num, '번째 수는', item, '입니다')

# if sum != 15:
#    break
# 이런거 안됌 

line_x=[]
for i in range(1, 10):
   print()
   print(f'{i}단 시작 =========================')
   for j in range(1, 10):
      print(f'{i} X {j} = {i*j:>2}', end=' ')  