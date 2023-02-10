# 다이얼로그

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        # 자식 클래스(Student)가 상속받는 부모 클래스(Human)를 
        # 자식 클래스(Student)에 불러오겠다 는 의미
        self.initUI()

    def initUI(self):
       
        self.textEdit = QTextEdit(self)
        # 텍스트 에디터 만들기
        self.setCentralWidget(self.textEdit)

        self.statusBar()

        openFile = QAction('Open', self)
        # openFile의 액션은 Open이다.
        openFile.setShortcut('Ctrl+O')
        # openFile의 단축키는 Crtl+O로 지정한다.
        openFile.setStatusTip('파일열기')
        # openFile 바에 마우스를 올리면 파일 열기라고 알려줌
        openFile.triggered.connect(self.onClicked)

        menubar = self.menuBar()
        # 메뉴바 생성
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        # 메뉴바에 메뉴 추가 이름은 File
        fileMenu.addAction(openFile)
        # File 누르면 openFile이라는 함수 액션을 취한다.

        # 필수 배치
        self.setWindowTitle('파일 다이얼로그 위젯')
        self.setGeometry(300,300,300,300)
        self.show()

    def onClicked(self):
        fname = QFileDialog.getOpenFileName(self, '파일열기', './')
        # fname은 QFileDialog이고 읽어오는 파일은 당해 파일 이름은 파일열기
        if fname[0]: # 파일을 선택했다면
            file = open(fname[0], 'rt', encoding='utf-8')
            with file:
            # while로 해도 된다.
                data = file.read()
                # 파일을 읽어서 data에 저장
                self.textEdit.setText(data)
                # 텍스트를 읽어와서 표시

            file.close()

        QMessageBox.about(self, '성공', '로드했습니다.')
        # 메시지 띄워주는 명령어 많이 씀.

    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, '종료', '정말 종료하시겠습니까?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 메시지 박스로 물어본다, 끌꺼냐? 기본 세팅값은 아니요
        if reply == QMessageBox.Yes:
            # 그래도 끈다고 하면 이벤트 종료
            event.accept()
        else:
            # 아니면 그대로 유지
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())