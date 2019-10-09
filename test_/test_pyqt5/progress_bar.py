# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 0016 10:08
# @Author  : Noza
# @Email   : wz_spinoza@sina.com
# @File    : progress_bar.py
# @Software: PyCharm
import sys
import time
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon


class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    # 窗体GUI部分
    def init_ui(self):
        # 设置窗体大小
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('进度条')
        self.setWindowIcon(QIcon('pics/874176.png'))
        # 创建进度条
        self.pbar = QProgressBar(self)
        # 进图条位置及大小
        self.pbar.setGeometry(30, 10, 200, 25)
        # 创建开始按钮
        self.btn = QPushButton('开始', self)
        # 创建按钮并移动
        self.btn.move(30, 50)
        # 点击按钮，连接事件函数
        self.btn.clicked.connect(self.btn_action)
        # 创建重置按钮
        self.btn_reset = QPushButton('重置', self)
        self.btn_reset.move(125, 50)
        self.btn_reset.clicked.connect(self.btn_res)

        # 创建计时器
        self.timer = QBasicTimer()
        # 计时器赋初值
        self.step = 0

        # 隐藏按钮
        self.btn_hide = QPushButton('武军大傻子', self)
        self.btn_hide.setGeometry(30, 10, 170, 25)
        self.btn_hide.clicked.connect(self.btn_hide_)
        self.btn_hide.hide()
        # 显示
        if time.time() > 1540049163:
            self.msg_box = QMessageBox.warning(self, '警告！', '软件已过期,请联系作者！', QMessageBox.Yes)
        else:
            self.show()

    def close_app(self):
        if self.msg_box == QMessageBox.Yes:
            sys.exit(app.exec_())
    # 按钮点击
    def btn_action(self):
        # 如果计时器处于激活状态
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            # 参数100是进度条进行速度，值越大速度越慢
            self.timer.start(10, self)
            self.btn.setText('停止')

    def btn_res(self):
        self.timer.stop()
        self.step = 0
        self.pbar.setValue(self.step)
        self.pbar.show()
        self.btn_hide.hide()
        self.btn.setText('开始')
        self.btn_hide.setText('武军大傻子')
        self.btn_hide

    def btn_hide_(self):
        self.btn_hide.setText('武军特别傻')

    # 计时器事件,timerEvent是原有函数，这里对它进行重写
    def timerEvent(self, *args, **kwargs):
        if self.step > 100:
            self.timer.stop()
            self.btn.setText('完成')
            self.pbar.hide()
            self.btn_hide.show()
            return
        self.step += 1
        self.pbar.setValue(self.step)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pbar = ProgressBar()
    sys.exit(app.exec_())

