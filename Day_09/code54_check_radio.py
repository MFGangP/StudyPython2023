# 체크박스, 라디오 버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        cbShowTitle = QCheckBox('Show Title', self)
        cbShowTitle.move(20, 20)    # 절대 배치
        cbShowTitle.toggle()

        # signal 종류 stateChanged
        # connect() 매개변수 -> 슬롯함수
        cbShowTitle.stateChanged.connect(self.changeTitle)

        cbKorea = QCheckBox('한국', self)
        cbKorea.move(20, 60)
        cbKorea.stateChanged.connect(self.checkKorea)
        
        # 라디오 버튼
        rbtn = QRadioButton('남성', self)
        rbtn.move(120,20)
        rbtn.setChecked(True)

        rbtn = QRadioButton('여성', self)
        rbtn.move(120,40)

        # 필수 배치
        self.setWindowTitle('버튼')
        self.setGeometry(300,300,300,300)
        self.show()

    # 슬롯함수 - 시그널을 처리하는 함수
    def changeTitle(self, state):
        if state == Qt.CheckState.Checked:  # Qt.Checked도 사용 가능
            self.setWindowTitle('체크박스 체크')
        else:
            self.setWindowTitle('체크박스 체크해제')

    def checkKorea(self, state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('나는 한국인')
        else:
            self.setWindowTitle('나는 머지?')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())