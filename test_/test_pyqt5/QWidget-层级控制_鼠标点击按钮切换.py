import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Label(QLabel):
    def mousePressEvent(self, ev) -> None:
        self.raise_()  # 鼠标按下后，将出发置顶事件


app = QApplication(sys.argv)

win = QWidget()
win.resize(600, 480)

win.setWindowTitle('鼠标点击按钮切换')

lable1 = Label(win)
lable1.setText('标签1')
lable1.resize(200, 200)  # 设置标签大小
lable1.setStyleSheet('background-color:red')

lable2 = Label(win)
lable2.setText('标签1')
lable2.resize(200, 200)  # 设置标签大小
lable2.setStyleSheet('background-color:green')
lable2.move(100, 100)

win.show()
sys.exit(app.exec())
