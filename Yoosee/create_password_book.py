import itertools
import string
import os
import time


def get_words():
    '''
    生成字符
    :return:
    '''
    print(string.digits)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)


def cread_password_book(words, pwd_len):
    '''
    生成密码本
    :param words: 字符集
    :param pwd_len: 密码长度
    :return:
    '''
    # 删除已有文件
    my_file = 'password_book.txt'  # 文件路径
    if os.path.exists(my_file):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(my_file)  # 则删除

    # 生成密码
    passwords = itertools.product(words, repeat=pwd_len)
    for password in passwords:
        password = ''.join(password)
        print(password)
        with open('password_book.txt', 'a+') as f:
            f.write(password + '\n')


start = time.time()

# 包含的密码字符
# words = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
words = '0123456789'
cread_password_book(words, 3)

end = time.time()
print('密码本生成用时：{}'.format(end - start))
