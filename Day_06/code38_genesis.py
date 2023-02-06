# Car 클래스를 상속한 제네시스 클래스

from code37_car import Car

#Child class
class Genesis(Car):
    def __init__(self, name, color, 
                 plate_number, product_year) -> None:
        super().__init__()
    # 부모클래스가 가지고있는 init을 가져와라

        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = product_year
        print(f'{self.__name} 인스턴스 생성!')

    # 부모가 가지고있는걸 다 쓸수있지만 없는거도 만들어서 쓸 수 있다.
    # 부모가 가지고있는 걸 가져와서 재정의를 해서 써야함
    # 더 좋게 만들 수 있다는 뜻

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def run(self):
        return f'{self.__name}이(가) 달립니다.'
    # 재정의

    def stop(self):
        return f'{self.__name}이(가) 멈춥니다'

gv80 = Genesis('팔공이', 'black', '66오 1004', 2022)
# gv80.set_name('팔공이')
print(f'이 차의 이름은 {gv80.get_name()}입니다.')
print(gv80.run())
print(gv80.stop())

# 부모가 가지고있는 함수를 재정의 해서 사용

# @ 데코레이터 라는게 있다.

# 추상 클래스 - 내용 없이 사용할 함수 이름만 알려줌
# 재정의해서 쓸 거기 때문에 대략적인 틀만 제시