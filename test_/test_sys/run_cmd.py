import os
import pandas as pd

# 删除已有文件
def
my_file = 'ip_arr.xlsx'  # 文件路径
if os.path.exists(my_file):  # 如果文件存在
    # 删除文件，可使用以下两种方法。
    os.remove(my_file)  # 则删除

cmd = 'netstat -a -n'
test = os.popen(cmd)
text = test.read().split('\n')
# print(text)

for i in text:
    # 获得TCP IP地址
    if i[:5] == '  TCP':
        x = i.split('    ')
        print('TCP-{}'.format(x[1]))
    elif i[:5] == '  UDP':
        x = i.split('    ')
        print('UDP-{}'.format(x[1]))
