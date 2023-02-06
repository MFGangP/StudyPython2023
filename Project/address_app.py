# 주소록 앱
# 2023-02-06
# 박성현
# 15. 예외처리
# 15-1. 파일 없을 때 나는 예외
# 15-2. 입력시 / 개수가 다를 때 나는 예외
# 15-3. 메뉴 번호 입력 숫자 외 예외

import os # 운영체제용 모듈

# 2. 클래스 생성

class Contact:
    # 클래스 줄맞추기 주의
    # 생성자 - 이름, 전번, 이메일, 주소
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

    # 4. __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름 : {self.__name}\n'
                   f'핸드폰 : {self.__phone_num}\n'
                   f'이메일 : {self.__email}\n'
                   f'주  소 : {self.__addr}')   
        return str_res

    # 10. 객체 존재여부 확인 클래스 함수 
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            False

    # 12. 각 멤버 변수에 접근하는 함수
    #getName, gerPhone_num, get_Email, get_Addr
    def getName(self) -> str:
        return self.__name

    def getPhone_Num(self) -> str:
        return self.__phone_num

    def getEmail(self) -> str:
        return self.__email

    def getAddr(self) -> str:
        return self.__addr


# 5. 사용자 입력
def set_contact():
    name, phone_num, email, addr =  input('정보 입력(이름/전화번호/이메일/주소) : ').split('/')
    # print(name,phone_num,email,addr)
    # 7. contact 객체 만들기
    contact = Contact(name, phone_num, email, addr)
    # name=name 이렇게도 가능
    return contact

# 9. 주소록 출력
def get_contacts(list):
    for item in list:
        print(item)
        print('==========================')

# 10. 주소록 삭제
def del_contact(list, name):
    # enumerate 1번 2번 번호를 정해주는 클래스
    # 리스트 인덱스 추가생성
    count = 0 # 11. 찾는 이름 카운트
    for i, item in enumerate(list):
        if item.isNameExist(name):
            count += 1
            del list[i] # 리스트 삭제

    if count > 0 : # 11. 메세지 출력
        print('연락처를 삭제했습니다.')
    else:
        print('삭제할 연락처가 없습니다.')

# 13. 주소록 파일 저장
def save_contacts(list):
    file = open('C:\Source\studypython2023\Project\contacts.txt',
                'w',encoding='utf-8')
    for item in list:
        text = f'{item.getName()}/{item.getPhone_Num()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')
    # file.write(f'{text}\n') 이렇게 되면 한 줄만 저장 됌
    # 줄 구분 똑바로 해야 저장 할 때 제대로 된다.
    file.close() # 파일 닫아줘야 함!

# 14. 주소록 파일 불러오기
def load_contacts(list):
    try:        
        file = open('C:\Source\studypython2023\Project\contacts.txt',
                    'r',encoding='utf-8')
    except Exception as e:  # 15-1. 예외처리
        f = open('C:\Source\studypython2023\Project\contacts.txt',
                    'w',encoding='utf-8')
        f.close()   # 파일이 없어서 생기는 예외는 파일 생성하고
                    # 함수를 빠져나감
        return
        # 리턴문으로 while 거치지 않고 함수를 빠져나가서
        # 오류가 없음

    while True:
        line = file.readline().replace('\n','') # 15. 문장 끝 \n 제거
        if not line: break

        lines = line.split('/')
        contact = Contact(lines[0],lines[1],lines[2],lines[3])
        list.append(contact)

    file.close()

# 추가. 화면 클리어
def clear_console():
    command = 'clear' # Linux, Unix 화면 클리어 명령어
    if os.name in ('nt', 'dos'): # Window 운영체제라면
        command = 'cls' # 윈도우 화면 클리어 명령어
        os.system(command)
        
# 6. 메뉴표시
def get_menu():
    str_menu = ('주소록 앱 v0.3\n'
                '1.연락처 추가\n'
                '2.연락처 출력\n'
                '3.연락처 삭제\n'
                '4.앱 종료\n')
    print(str_menu)
    try:
        menu = int(input('메뉴 입력 : '))
    except Exception as e:
        menu = 0
    # 사용자가 뭘 잘못 넣든 0으로 바껴서 넘어감
    # 15-3 숫자 외 입력예외 처리
    # 영문자, 특수문자 넣으면 전부 0으로
    return menu    

# 3. 전체 실행
def run():
    contacts = list()   # 주소를 담기위한 빈 리스트 생성
    load_contacts(contacts) # 14. 주소록 읽어오기
    # temp = Contact('박성현', 
    #                '010-1234-1234', 
    #                'lovehyun95@naver.com', 
    #                '부산시 남구 ...')
    # print(temp)
    # set_contect()
    clear_console()
    
    while True:
        sel_menu = get_menu()
        if sel_menu == 1:   # 8. 연락처 추가
            try:    # 15-2 연락처 입력 잘못했을 시 예외처리
                # clear_console() # 화면 클리어는 취향 차이
                contact = set_contact()
                contacts.append(contact)
                input('저장되었습니다.') # 아무것도 안받는 입력
                clear_console()
            except Exception as e:
                input('올바른 정보를 입력해주세요(이름/전화번호/이메일/주소)')
            finally:
                clear_console()

        elif sel_menu == 2:
            clear_console()
            get_contacts(contacts)
            input('주소록 출력 완료') # 아무것도 안받는 입력
            clear_console()

        elif sel_menu == 3:
            clear_console() # 10. 연락처 삭제
            name = input('삭제할 이름 입력 : ')
            del_contact(contacts, name)
            input()
            clear_console()

        elif sel_menu == 4: # 앱 종료
            save_contacts(contacts) # 13. 종료시 주소록 파일 저장
            break

        else:
            input('올바른 메뉴를 선택해주세요.')
            clear_console()

# 1. 메인 실행 영역
if __name__ == '__main__':
    run()