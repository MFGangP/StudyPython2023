# 체크박스, 라디오 버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblOption = QLabel('선택값 : ', self)
        # self를 빼면 initUI의 변수(로컬 변수)
        # 이 함수(initUI) 안에서만 도는 변수
        # self = MyApp
        # self를 넣어야 글로벌 변수(전역변수)
        # 내 클래스(MyApp)에 속하는 변수로 만들게
        self.lblOption.move(20, 20)

        cbOtion = QComboBox(self)
        cbOtion.addItem('Option1')
        cbOtion.addItem('Option2')
        cbOtion.addItem('Option3')
        cbOtion.addItem('Option4')
        cbOtion.move(20, 40)

        cbOtion.activated[str].connect(self.onActivated)

        # 필수 배치
        self.setWindowTitle('Combo Box')
        self.setGeometry(300,300,300,300)
        self.show()

    # 슬롯 변수
    def onActivated(self, text):
        self.lblOption.setText('선택값 : ' + text)
        self.lblOption.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())