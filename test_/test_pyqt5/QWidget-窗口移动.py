import sys
from PyQt5.Qt import *


class Win(QWidget):
    def __init__(self):
        super().__init__()
        # 设置一个标记，用来判定事件是否被触发
        self.move_flag = False

        self.setWindowTitle('设置窗口移动')
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pass

    def mousePressEvent(self, ev) -> None:
        # 如果左键被按下
        if ev.button() == Qt.LeftButton:
            self.move_flag = True
            # 取出鼠标点击后，相对于桌面的坐标
            self.table_x = ev.globalX()
            self.table_y = ev.globalY()
            # 取出窗体坐标（左上角）
            self.win_x = self.x()
            self.win_y = self.y()

    def mouseMoveEvent(self, ev) -> None:
        if self.move_flag:
            # 获取鼠标移动向量数据
            move_x = ev.globalX() - self.table_x
            move_y = ev.globalY() - self.table_y
            # 获取窗体最新坐标
            win_move_x = self.win_x + move_x
            win_move_y = self.win_y + move_y
            # 设置窗体移动
            self.move(win_move_x, win_move_y)
            # 设置窗体透明度
            self.setWindowOpacity(.7)

    def mouseReleaseEvent(self, ev) -> None:
        self.move_flag = False
        # 恢复窗体不透明
        self.setWindowOpacity(1)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())
