# 라이프 스코프

a = 1 # 변수

# 함수 더블클릭하면 이름 전체 선택 가능
# 함수 뒤에 커서 두고 이름 바꾸고 싶으면 F2번
# 동일한 함수 전체 다 똑같은 이름으로 바꿔줌
# 동일한 함수 이름 사이에서 자리 이동 F7

def vartest(a):
#   global a        전역(global)에 있는 a를 함수(local)에 가져다 쓴다  
#   SyntaxError: name 'a' is parameter and global
    a = a + 1   # 매개변수
    return a  

a = vartest(a)

print(a)