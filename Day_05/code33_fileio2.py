# 파일 읽어오기

file = open('./fileiotest/sample01.txt', 'r', encoding='utf-8')
while True:
    
    text = file.readline()

    if not text:
        break

    else:
        print(text)

file.close