# 스타일
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 스타일 설정
        lbl_red = QLabel('Red')
        lbl_red.setStyleSheet('color: red;'
                              'border-style: solid;'
                              'border-width: 5px;'
                              'border-color: #FA8072;'# 색깔 코드는 16진수 2자리 곱한 값이 250 아래의 수
                              'border-radius: 10px;')

        lbl_green = QLabel('Green') 
        lbl_green.setStyleSheet('color: grren;'
                              'border-style: dashed;'
                              'border-width: 5px;'
                              'border-color: #7FFFD4;')

        # 레이아웃을 세로 구분짓는 레이아웃
        vbox = QVBoxLayout() # QVBoxLayout 세로 / QHBoxLayout 가로
        # 위젯 추가
        vbox.addWidget(lbl_red) 
        vbox.addWidget(lbl_green) 
        # 전체 레이아웃에 vbox를 추가
        self.setLayout(vbox)

        self.setWindowTitle('스타일 지정')
        # 기본 설정 - 사이즈, show() = 필수!
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())