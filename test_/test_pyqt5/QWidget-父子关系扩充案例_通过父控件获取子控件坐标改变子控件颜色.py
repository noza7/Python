import sys
from PyQt5.Qt import *


class Win(QWidget):
    def mousePressEvent(self, ev) -> None:
        # 获得窗口内部相对坐标
        local_x = ev.x()
        local_y = ev.y()
        print(local_x, local_y)
        # 获取子控件坐标
        sub_widget=self.childAt(local_x,local_y)
        # 判定：如果子控件存在
        if sub_widget is not None:
            sub_widget.setStyleSheet('background-color:red;')


# 创建应用程序对象
app = QApplication(sys.argv)
# 创建控件
win = Win()
win.setWindowTitle('父子关系案例')
win.resize(500, 500)

for i in range(5):
    label = QLabel(win)
    label.setText('标签{}'.format(i + 1))
    label.move(100, 50 * i)
win.show()
sys.exit(app.exec())
