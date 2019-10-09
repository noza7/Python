import sys
from PyQt5.Qt import *


# 重写标签事件
class Label(QLabel):
    # 通过重写鼠标按压事件
    def mousePressEvent(self, ev) -> None:
        # 改变标签的背景颜色
        self.setStyleSheet('background-color:red;')


# 创建应用程序对象
app = QApplication(sys.argv)
# 创建控件
win = QWidget()
win.setWindowTitle('父子关系案例')
win.resize(500, 500)

for i in range(5):
    label = Label(win)
    label.setText('标签{}'.format(i + 1))
    label.move(100, 50 * i)
win.show()
sys.exit(app.exec())
