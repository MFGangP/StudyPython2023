# 다이얼로그

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        # 자식 클래스(Student)가 상속받는 부모 클래스(Human)를 
        # 자식 클래스(Student)에 불러오겠다 는 의미
        self.initUI()

    def initUI(self):
        self.btnDlg = QPushButton('Dialog', self)
        # 다이얼 로그 버튼을 만듦
        self.btnDlg.move(30, 30)
        # 위치 이동
        self.btnDlg.clicked.connect(self.onBtnDlgClicked)
        # 클릭했을 때 슬롯함수는 onBtnDlgClicked
        self.txtInput = QLineEdit(self)
        # 텍스트 입력을 받을 라인 에디트 생성
        self.txtInput.move(30, 60)
        # 위치이동

        # 필수 배치
        self.setWindowTitle('다이얼로그 위젯')
        self.setGeometry(300,300,300,300)
        self.show()

    def onBtnDlgClicked(self):
        text, ok = QInputDialog.getText(self, '인풋 다이얼로그', '이름을 적으세요')
        # 튜플로 값을 받는데 ok 누르면 True, cancle 누르면 False

        if ok:
            self.txtInput.setText(text)
            # 다이얼로그에다 텍스트를 입력하면 txtInput에 넣어준다.

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())