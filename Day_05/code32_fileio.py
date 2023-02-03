# 파일 만들기

file = open('sample.txt','w') # 파일 쓰기로 만듦

file.write('퇴근 반대')
file.write('다시 출근하세요')

file.close()
print('sample.txt가 생성되었습니다.')

# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라 언어를 다 표현 가능