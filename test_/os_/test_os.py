import os

# 打印扩展名为".txt"的所有文件
for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)
