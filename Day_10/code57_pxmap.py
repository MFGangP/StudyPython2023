# 이미지처리 위젯

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
        pixmap = QPixmap('./Day_10/image.jpg').scaledToWidth(640) # .scaledToHeight() 둘 중 하나
        # 파일 불러와서 사이즈 조절
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Qt.Aligncenter 사용가능

        vbox = QVBoxLayout(self)
        # 이미지 밑에 글자 넣으려고 vbox에 넣음
        vbox.addWidget(lblImage)
        # 이미지 
        vbox.addWidget(lblSize)
        # 이미지 크기 나타내는 텍스트
        self.setLayout(vbox)
        
        # 필수 배치
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(300,300,300,300)
        self.show()
        # self.showFullScreen() 전체화면 

    def setCenter(self):
        qr = self.frameGeometry()   # 창 자기 자신의 위치값 
        cp = QDesktopWidget().availableGeometry().center()  # 모니터 화면 중심
        qr.moveCenter(cp)
        # 창 자기자신의 위치값을 센터로 옮긴 뒤에 왼쪽 위로 정렬
        self.move(qr.topLeft())     

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())