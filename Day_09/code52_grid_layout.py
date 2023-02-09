# 레이아웃 절대적 배치

import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(QLabel('Title'), 0, 0) # '열'row = 0,'행'col = 0
        grid.addWidget(QLabel('Author'), 1, 0)# 1, 0
        grid.addWidget(QLabel('Rewiew'), 2, 0)# 2, 0

        grid.addWidget(QLineEdit(), 0, 1) # 0행 1열
        grid.addWidget(QLineEdit(), 1, 1) # 1행 1열
        grid.addWidget(QTextEdit(), 2, 1) # 2행 1열

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

        grid.addWidget(btnOk, 3, 0)
        grid.addWidget(btnCancel, 3, 1)
    
        # 필수 배치
        self.setWindowTitle('박스 배치')
        self.setGeometry(300,300,300,300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())