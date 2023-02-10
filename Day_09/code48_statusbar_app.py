import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime
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

        actSave = QAction(QIcon('./Day_09/save.png'), 'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        actPrint = QAction(QIcon('./Day_09/print.png'),'Print', self)
        actPrint.setShortcut('Ctrl+P')
        actPrint.setStatusTip('출력')

        actEdit = QAction(QIcon('./Day_09/edit.png'),'Edit', self)
        actEdit.setShortcut('Ctrl+E')
        actEdit.setStatusTip('설정')
        

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar')    # 툴바 타이틀은 없어도 됨
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)
        toolbar.addAction(actPrint)
        toolbar.addAction(actEdit)

        # 상태바
        now = QDate.currentDate() # 현재 날짜
        time = QTime.currentTime() # 현재 시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd-dddd'+ ' ' + time.toString('hh:mm:ss')))
        self.setWindowIcon(QIcon('./Day_09/space.png'))

        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        # 메서드는 타이틀바에 나타나는 창의 제목을 설정합니다.
    # self.move(1980 // 2 - 200, 1080 // 2 - 100)
        # 메서드는 위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
        # 정중앙 위치잡기
        # 해상도는 모두 정수
        self.resize(400, 200) # y = 400, x = 200 
        # GUI 화면을 설정해줘야된다.
        # 메서드는 위젯의 크기를 너비 400px, 높이 200px로 조절합니다.
        
        # 화면 중앙에다가 세팅해라
        self.setCenter()
        
        self.show() # 핵심!!  보여준다.
        # 메서드는 위젯을 스크린에 보여줍니다.
        
    # 화면 중심 셋팅
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