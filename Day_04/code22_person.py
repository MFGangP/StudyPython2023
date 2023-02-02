# 클래스 생성

class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'O'

    def walk(self):
        print('걷습니다.')
        return

    def run(self, option):
        self.walk()
        if option == 'Fast':
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!.')
        return

    def stop(self):
        print('멈춥니다.')
        return

park = Person() # 객체를 instance라고 함
park.name = '박성현'
park.height = '175'
park.gender = 'male'
park.blood_type = 'RH+ O'
# 이렇게 하나를 지칭하는 구조를 만듦

print(f'{park.name}의 혈액형은 {park.blood_type}입니다.')

park.run('Fast')