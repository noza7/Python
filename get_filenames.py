# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 0017 12:41
# @Author  : Noza
# @Email   : wz_spinoza@sina.com
# @File    : output_excel.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 0016 10:08
# @Author  : Noza
# @Email   : wz_spinoza@sina.com
# @File    : progress_bar.py
# @Software: PyCharm
import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QPushButton, QFileDialog, QLabel, QFrame, QMessageBox, \
    QInputDialog, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import openpyxl


# git测试
# 第二次修改
# 第三次修改

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        '''
        # 窗体GUI部分
        :return:
        '''
        # 设置窗体大小
        self.setGeometry(500, 200, 350, 200)
        # 设置固定大小
        self.setFixedSize(490, 370)
        self.setWindowTitle('文件名称提取程序')
        self.setWindowIcon(QIcon('icon/769160.png'))
        self.setMinimumHeight(800)

        # 设置软件过期时间
        data = '2019-8-21 13:50:00'
        data_array = time.strptime(data, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(data_array))
        # print(timeStamp)
        # 判断软件是否过期
        if time.time() > timeStamp:
            QMessageBox.warning(self, '', '软件已过期，请联系作者', QMessageBox.Yes)
        else:
            # 进度条
            self.pbar = QProgressBar(self)
            # 进图条位置及大小
            self.pbar.setGeometry(20, 200, 480, 20)

            # todo 按钮
            # 选择文件按钮
            self.btn_select_file = QPushButton('选择文件夹', self)
            self.btn_select_file.move(20, 230)
            self.btn_select_file.setFixedSize(125, 20)
            self.btn_select_file.clicked.connect(self.file_dialog)
            # 输出文件按钮
            self.btn_output_path = QPushButton('选择输出文件夹', self)
            self.btn_output_path.move(20, 270)
            self.btn_output_path.setFixedSize(125, 20)
            self.btn_output_path.clicked.connect(self.output_dialog)
            # 开始按钮
            self.btn = QPushButton('开始', self)
            # 创建按钮并移动
            self.btn.move(150, 310)
            self.btn.setFixedSize(200, 40)
            # 点击按钮，连接事件函数
            self.btn.clicked.connect(self.btn_action)

            # todo 标签
            # 文件路径标签
            self.lab_select_path = QLabel('文件路径', self)
            self.lab_select_path.move(150, 230)
            self.lab_select_path.setFixedSize(320, 20)
            self.lab_select_path.setFrameShape(QFrame.Box)
            self.lab_select_path.setFrameShadow(QFrame.Raised)
            # 输出标签
            self.lab_output_path = QLabel('文件路径', self)
            self.lab_output_path.move(150, 270)
            self.lab_output_path.setFixedSize(320, 20)
            self.lab_output_path.setFrameShape(QFrame.Box)
            self.lab_output_path.setFrameShadow(QFrame.Raised)
            # 说明标签
            content = '说明:\n    选择需要提取名称的文件夹；选择输出结果文件夹。\n'
            self.description_lab = QLabel(content, self)
            self.description_lab.move(20, 10)
            self.description_lab.setFixedSize(450, 170)
            self.description_lab.setAlignment(Qt.AlignTop)
            self.description_lab.setFrameShape(QFrame.Box)
            self.description_lab.setFrameShadow(QFrame.Raised)
            # 自动换行
            # self.description_lab.adjustSize()
            self.description_lab.setWordWrap(True)

            self.step = 0

            # 显示
            self.show()

    # 按钮点击
    def btn_action(self):
        if self.btn.text() == '完成':
            self.close()
        else:
            file_path = '{}'.format(self.lab_select_path.text())
            output_path = '{}'.format(self.lab_output_path.text())
            password = ('123', True)

            ok = QInputDialog.getText(self, "Noza", "请输入密码：", QLineEdit.Password, '')
            if ok == password:
                if self.btn.text() == '开始':
                    if not os.path.exists(file_path):
                        QMessageBox.warning(self, '', '请选择路径', QMessageBox.Yes)
                    elif not os.path.exists(output_path):
                        QMessageBox.warning(self, '', '请选择输出路径', QMessageBox.Yes)
                    else:
                        self.btn.setText('程序进行中')
                        self.run()
            else:
                QMessageBox.warning(self, '', '密码不正确！！！', QMessageBox.Yes)

    # 选择输入文件路径
    def file_dialog(self):
        # './'表示当前路径
        path = QFileDialog.getExistingDirectory(self, '选取文件', './')
        # 标签框显示文本路径
        self.lab_select_path.setText(path)
        # 自动调整标签框大小
        self.lab_select_path.adjustSize()

    # 选择输出路径
    def output_dialog(self):
        path = QFileDialog.getExistingDirectory(self, '选取文件', './')
        # 标签框显示文本路径
        self.lab_output_path.setText(path)
        # 自动调整标签框大小
        self.lab_output_path.adjustSize()

    def set_progerss_bar(self, num):
        '''
        设置进图条函数
        :param num: 进度条进度（整数）
        :return:
        '''
        self.step = num
        self.pbar.setValue(self.step)

    # 业务逻辑
    def run(self):
        # todo  文件路径
        file_path = '{}'.format(self.lab_select_path.text())
        output_path = '{}'.format(self.lab_output_path.text())

        # todo
        def get_file_name(file_dir):
            '''
            获取指定目录下所有文件名称
            :param file_dir:指定目录
            :return:返回文件名列表
            '''
            for root, dirs, files in os.walk(file_dir):
                # return root#当前目录路径
                # return dirs#当前路径下所有子目录
                return files  # 当前路径下所有非目录子文件

        self.set_progerss_bar(10)

        def output2excel(file_dir, output_path):
            '''
            把文件夹下的文件名称输出到文件目录
            :param file_dir: 文件目录
            :return:
            '''

            # 获取文件目录下所有文件名，存入data列表
            data = get_file_name(file_dir)

            self.set_progerss_bar(50)

            # 把data输出到该目录下，并以目录名保存为excel格式
            wb = openpyxl.Workbook()
            sheet = wb.active
            # 设置表名为文件目录名
            sheet.title = '生成结果'
            for i in range(1, len(data) + 1):
                sheet['A{}'.format(i)] = data[i - 1]

            self.set_progerss_bar(80)

            wb.save('{0}/生成结果.xlsx'.format(output_path))

        output2excel(file_path, output_path)
        self.set_progerss_bar(100)
        self.btn.setText('完成')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pbar = MainUI()
    sys.exit(app.exec_())
