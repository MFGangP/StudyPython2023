# 자동차 클래스

import os
import code22_person

class Car:

    __number = '54라 9538'
    # 이 변수에 직접적으로 접근하지말라.

    def get_number(self) -> str:
        return self.__number

    # 클래스 외부에선 변경 X, 멤버 함수로는 내부를 조작 O
    def set_number(self, number):
        self.__number = number

    def __init__(self, number = '54라 9538') -> None:
        print('__init__')
        self.__number = number
 
    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls) # 부모 클래스 (상속)

    # 부모 클래스 생성자를 생성해서 new를 실행해라
    # new는 새로운 클래스를 만듦 - 얘가 진짜 생성자(잘 안씀)
    # init은 초기화 할 때 새로운 변수 값 할당 - 근데 얘가 생성자라 부름

    def __str__(self) -> str:
        return f'제 차 번호는 {self.__number}입니다. ' 

yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number = '54라 9999'  # 외부에서는 멤버변수에 접근 불가
print(yourcar)
print('클래스 내부 함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제 차는 아이오닉이고, 번호는 {mycar.get_number()}입니다.')

mycar.__number = '132거 8874'
print(mycar.get_number())
print(mycar)

# 외부(객체)에서 클래스 내부의 속성값을 못바꾸게 하는 것
# 캡슐화
# 개발자의 권한을 못 건드리게 만드는것