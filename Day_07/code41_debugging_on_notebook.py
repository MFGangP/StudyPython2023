# %% [markdown]
# ## 7일차
# - 셀 오른쪽 아래에서 언어 변경 가능
#     - 마크다운, 파이썬, SQL 등등...
# - 셀이 선택된 상태에서는 변경할 수 없음 
# - ESC 눌려서 선택 해제 하고 난뒤에 변경 가능
# - 다 작성하면 Ctrl + Enter로 빠져 나와야함
# >
# 단축키
# >
# - a : 위에 새로운 셀 추가
# - b : 아래에 새로운 셀 추가
# 
#     - c : 셀 복사하기
#     - v : 셀 붙여넣기
#     - x : 셀 잘라내기
#     - dd : 셀 삭제하기
#     - p : 셀 아래에 붙여넣기
# >
# - 포커스(커서가 깜박거리지 않는)상태에서 M(마크다운), Y(프로그램 언어)
# 
#     - Shift + m : 선택 셀과 아래 셀과 합치기
#     - Ctrl + s 또는 s  : 파일 저장
#     - Enter  : 선택 셀의 코드 입력 모드로 돌아가기
# >
# - Ctrl + Enter : 입력 셀 실행
# >
# ### 둘 다 이전 셀을 상속해서 셀을 생성함
# - Alt + Enter : 입력영역 실행 후(셀 실행) 아래 새로운 영역 추가(다음 셀 생성) 밑에 셀 무조건 생성
# - Shift + Enter : 입력 셀 실행 후 아래 셀로 이동 (없으면 새로운 셀 추가) 밑에 셀 있으면 안만듦    
# 
#     - Ctrl + a : 선택 셀의 코드 전체 선택
#     - Ctrl + z : 선택 셀 내 실행 취소
#     - Ctrl + y : 선택 셀 내 다시 실행
# >
# - Ctrl + / : 커서 위치 라인 주석처리
# 
#     - Shift + Ctrl + - : 커서 위치에서 셀 둘로 나누기

# %%
print('Hello, Jupyter!!')
# print('Hello, Jupyter!!')

# %% [markdown]
# ## 디버깅 - 제일 중요함
# 
# 파이썬 디버깅에는 제약사항이 없음
# 주피터 노트북에서는 

# %%
arr = [1, '2', True, 'hello', 3.1415926585]
for i in arr:
    print(i)

# %% [markdown]
# ## 함수 디버깅

# %%
def plus(x, y):
    val = x + y
    return val

def div(x, y):
    val = x / y
    return val
    
print('더하기')
print(plus(10, 4))

# %%
print('나누기')
# print(div(10,0))

print(arr)
arr
# %%
