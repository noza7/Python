import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)

win = QWidget()
win.resize(600, 480)
icon=QIcon('pics/10christmas_lable_09.png')
win.setWindowIcon(icon)
win.show()
sys.exit(app.exec())
