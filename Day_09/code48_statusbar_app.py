import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,qApp,QAction
from PyQt5.QtGui import QIcon

# MyApp이라는 클래스를 만들 껀데 QWidget한테 상속 받을거야
class MyApp(QMainWindow):

    def __init__(self, ):
        super().__init__()
        # UI 실행
        self.initUI()

    def initUI(self, ):
        # 액션
        actExit = QAction(QIcon('./Day_09/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q')   # 단축키 지정
        actExit.setStatusTip('앱 종료')
        actExit.triggered.connect(qApp.quit) # 종료

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 상태바
        self.statusBar().showMessage('statusbar message')
        self.setWindowTitle('Bar Window')
        # 메서드는 타이틀바에 나타나는 창의 제목을 설정합니다.
        self.move(1980 // 2 - 200, 1080 // 2 - 100)
        # 메서드는 위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
        # 정중앙 위치잡기
        # 해상도는 모두 정수
        self.resize(400, 200) # y = 400, x = 200 
        # GUI 화면을 설정해줘야된다.
        # 메서드는 위젯의 크기를 너비 400px, 높이 200px로 조절합니다.
        self.show() # 핵심!!  보여준다.
        # 메서드는 위젯을 스크린에 보여줍니다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())