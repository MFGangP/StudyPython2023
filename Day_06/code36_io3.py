# 콘솔출력 보충
# 이스케이프 캐릭터(탈출문자)
# 안쓰면 한 줄로 쭉 나온다.
# 캐리지 리턴 - 줄 바꾼 뒤에 커서를 문장 앞으로 당기는 역할

print('1. Hello.\r\nWorld') # 리눅스 아니면 똑같다
print('2. Hello.\nWorld')   # 이걸 권장

print('3. Hello.\n\tWorld')    # t 탭
print('4. Hello.\n\t\bWorld')  # b 백스페이스
print('5. Hello.\n\'World\'')  # \' 문자열네 홑따옴표
print('6. Hello."World"')      # 
print('7. Hello.\"World\"')    # \" 쌍따옴표
print('8. Hello.\ "World"')    # 파이썬은 역슬래시가 그냥 표시가 된다.
print('9. Hello.\\"World"')    # \를 문자열에 표현

print('10.Hello.\0')           # \0 문자열이 끝났다는걸 알려준다.

# 문자열 포맷팅 - 구닥다리
# %로 포맷코드를 시작

me = '저'
name = '성명건'
age = 40
print('%s는 %s입니다. %d대 입니다.'% (me, name, age))

print(f'{254.112233:.2f}')     # 최신식

print('%4.4f' %(254.112233))     # 구식
# 정수 전체 자리수 4자리, 소수점 4자리 만들기