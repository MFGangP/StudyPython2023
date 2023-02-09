# 윈도우 창 닫기
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QToolTip, QMenuBar, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self,):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        btn = QPushButton('Quit', self)
        # 푸시버튼을 하나 만듭니다. 
        # 이 버튼 (btn)은 QPushButton 클래스의 인스턴스입니다.
        # 생성자 (QPushButton())의 첫 번째 파라미터에는 버튼에 표시될 텍스트를 입력하고, 두 번째 파라미터에는 버튼이 위치할 부모 위젯을 입력합니다.
        btn.move(322, 175)
        btn.resize(btn.sizeHint())
        # 버튼 툴팁
        btn.setToolTip('이거 누르면 그냥 꺼지니까 <b>조심해라.</b>')
        btn.clicked.connect(QCoreApplication.instance().quit)
        # PyQt5에서의 이벤트 처리는 시그널과 슬롯 메커니즘으로 이루어집니다. 버튼 (btn)을 클릭하면 'clicked' 시그널이 만들어집니다. instance() 메서드는 현재 인스턴스를 반환합니다. 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결됩니다. 이렇게 발신자 (Sender)와 수신자 (Receiver), 두 객체 간에 커뮤니케이션이 이루어집니다. 이 예제에서 발신자는 푸시버튼 (btn)이고, 수신자는 어플리케이션 객체 (app)입니다.
        self.setWindowIcon(QIcon('./Day_09/space.png'))
        self.setWindowTitle('Quit Button')
        # x 위치, y 위치, 너비, 높이, 
        self.setGeometry(1980 // 2 - 200, 1080 // 2 - 100, 400, 200)
        # 이 메서드는 창 띄우기 예제에서 사용했던 move()와 resize() 메서드를 하나로 합쳐놓은 것과 같습니다.
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())