import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

# MyApp이라는 클래스를 만들 껀데 QWidget한테 상속 받을거야
class MyApp(QWidget):

    def __init__(self, ):
        super().__init__()
        # UI 실행
        self.initUI()

    def initUI(self, ):
        self.setWindowTitle('Simple Window')
        # setWindowIcon() 메서드는 어플리케이션 아이콘을 설정하도록 합니다.
        # 아이콘 추가 - 파이썬은 작업 상위 폴더가 메인루트
        # 경로를 지정 해줘야한다.
        self.setWindowIcon(QIcon('./Day_09/space.png'))
        # setGeometry() 메서드는 창의 위치와 크기를 설정합니다.
        self.setGeometry(300, 300, 300, 300)
        # 메서드는 타이틀바에 나타나는 창의 제목을 설정합니다.
        self.move(1980 // 2 - 200, 1080 // 2 - 100)
        # 메서드는 위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
        # 정중앙 위치잡기
        # 해상도는 모두 정수
        self.resize(400, 200) # y = 400, x = 200 
        # GUI 화면을 설정해줘야된다.
        # 메서드는 위젯의 크기를 너비 400px, 높이 200px로 조절합니다.
        self.show() # 핵심!!  보여준다.
        # 메서드는 위젯을 스크린에 보여줍니다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())