# 객체지향 상속
# 클래스가 가지고있는 속성과 동작을 물려주는 것

# 차 부모클래스
class Car:
    # Mother Car

    __name = '자동차'
    __color = 'White'
    __plate_number = ''
    __product_yeat = 1900

    def get_name(self):
        return self.__name

    def __str__(self) -> str:
        return '부모 클래스'

    def run(self):
        return '차가 달립니다.'

    def stop(self):
        return '차가 멈춥니다.'    