import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

win = QWidget()
win.resize(600, 480)
win.show()
win.setWindowOpacity(.5)
win.setWindowTitle('设置窗体透明')
sys.exit(app.exec())
