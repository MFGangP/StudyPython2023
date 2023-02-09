# 푸시 버튼

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # & = Alt 누르면 메뉴 창 편하게 쓸 수 있게 해주는 세팅
        btn1 = QPushButton('&Button', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')
        # Alt + 2 누르면 토글되게 하는 세팅
        btn3 = QPushButton('Button', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)

        # 필수 배치
        self.setWindowTitle('버튼')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())