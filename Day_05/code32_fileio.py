# 글자 인코딩 encoding
# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라 언어를 다 표현 가능

# 파일 만들기

file = open('C:\\Source\\studypython2023\\fileiotest\\sample01.txt','w', encoding='UTF-8') # 파일 쓰기로 만듦
file = open('./fileiotest2/../fileiotest/sample02.txt','w', encoding='UTF-8')

file.write('퇴근 반대\n')
file.write('다시 출근하세요\n')
file.write('절대경로에 파일이 생성될겁니다.\n')

file.close()
print('sample1.txt가 생성되었습니다.')

# 파일/폴더 경로
