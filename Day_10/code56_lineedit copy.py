# 라인에디트 - Textbox

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblReasult = QLabel(self)
        self.lblReasult.move(10, 20)

        txtInput = QLineEdit(self)
        txtInput.setEchoMode(2) # 패스워드 모드
        txtInput.move(20, 40)
        txtInput.textChanged[str].connect(self.onChanged) 
        # 함수 이름 안쓰는 대신 [str]가 파라미터로 들어감

        # 필수 배치
        self.setWindowTitle('Line Edit')
        self.setGeometry(300,300,300,300)
        self.show()

    def onChanged(self, text):
        self.lblReasult.setText('입력값 : ' + text)
        self.lblReasult.adjustSize() # 라벨사이즈 자동

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())