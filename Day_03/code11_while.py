# while 문

hit = 0 # 변수 초기화 
        # while 문은 조심해서 쓸 것

while hit < 11:     # 원하는 조건 횟수보다는 커야함
    
    hit += 1    # hit를 1씩 증가
    print(f'나무를 {hit}번 찍었습니다.')

    if hit == 10:
        print('나무가 넘어갔습니다!!!')
        break
    else:
        print('나무가 아직 넘어가지 않았습니다. 끈질긴 놈')

print('나무 찍기 완료')