#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x
import itertools as its
import threading
# import rarfile
from unrar import rarfile
import os

# words = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 涉及到生成密码的参数
words = 'a01'
flag = True  # 是否关闭线程的标志


def append_on_file(password, file_name):
    # 把解析出的密码写入到文件中
    with open('password.txt', 'a', encoding='utf8') as f:
        text = file_name + ':' + password + '\n'
        f.write(text)


def get_password(min_digits, max_digits, words):
    """
    :param min_digits: 密码最小长度
    :param max_digits: 密码最大长度
    :param words: 密码可能涉及的字符
    :return: 密码生成器
    """
    while min_digits <= max_digits:
        pwds = its.product(words, repeat=min_digits)
        for pwd in pwds:
            yield ''.join(pwd)
        min_digits += 1


def extract(File, file_name):
    """
    若线程关闭标志为True，就执行循环，从密码生成器中取出密码，验证密码是否正确
    密码正确，则把密码写入文件中，并将线程关闭标志flag设定为False,通知其他线程关闭
    """
    global flag
    while flag:
        p = next(passwords)
        try:
            File.extractall(pwd=p)  # 打开压缩文件,提供密码...
            flag = False
            print("password is " + p)  # 破解到密码
            append_on_file(p, file_name)
            break
        except:
            print(p)


def mainStep(file_path, file_name):
    """
    多线程并发验证密码
    :param file_path: rar压缩文件路径列表
    :return:
    """
    file = rarfile.RarFile(file_path)
    print(file_path)
    for pwd in range(3):
        t = threading.Thread(target=extract, args=(file, file_name))
        t.start()


if __name__ == '__main__':
    # 主程序
    base_dir = r'C:\Python\crack_rar\rar'
    for file_info in os.listdir(base_dir):
        # print(file_info)
        try:
            # 拼接压缩文件路径
            file_path = os.path.join(base_dir, file_info)
            # 压缩文件名称
            file_name = file_info.split('.')[0]
            # 生成密码字典：密码长度最小为4，最大为11
            passwords = get_password(4, 4, words)

            # print(file_name)
            # 将任务分发给线程执行
            mainStep(file_path, file_name)
        except:
            pass
