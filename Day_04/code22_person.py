# 클래스 생성

class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'O'

    # __init__ 초기화 

    # 1. 생성자 추가 (기본값)
    # def __init__(self) -> None: # -> None = 리턴값이 없을 때 쓰는 것
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'
    #
    # 아래 방식으로 기본값 지정 해 줄 수 있음
    # 한 번도 사용안한 변수는 색이 연함

    def __init__(self, name = '홍길동', height = 170, gender = 'male'):
        self.name = name
        self.height = height
        self.gender = gender

    def walk(self):
        print(f'{self.name}이(가)걷습니다.')

    def run(self, option):
        self.walk()
        if option == 'Fast':
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!.')

    def stop(self):
        print(f'{self.name}이(가)멈춥니다.')

    # 2. 생성자 외 매직 메서드(function) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'



park = Person() # 객체생성을 한 실체 instance라고 함
park.name = '박성현'
park.height = '175'
park.gender = 'male'
park.blood_type = 'RH+ O'
# 이렇게 하나를 지칭하는 구조를 만듦

print(f'{park.name}의 혈액형은 {park.blood_type}입니다.')
print(park)
# park.run('Fast')

print('-------------------------------')

# 1. 초기화 후 객체생성
hong = Person()
hong.run('slow')
print(hong)

print('-------------------------------')

# 2. 파라미터를 받는 생성자 실행
ashely = Person('ashely', 170, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)
