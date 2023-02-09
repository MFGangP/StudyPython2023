# 레이아웃 절대적 배치

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOk = QPushButton('OK')
        btnCancel = QPushButton('Cancel')

        hbox = QHBoxLayout()# 가로로 버튼 세팅
        hbox.addStretch(1)  # 간격
        hbox.addWidget(btnOk) # ok 버튼
        hbox.addWidget(btnCancel) # 취소 버튼
        hbox.addStretch(1)  # 간격
        
        vbox = QVBoxLayout()# 가로박스 크게 하나 위쪽에 배치
        vbox.addStretch(3)  # 간격
        vbox.addLayout(hbox)# 버튼
        vbox.addStretch(1)  # 간격

        self.setLayout(vbox)

        # 필수 배치
        self.setWindowTitle('박스 배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())