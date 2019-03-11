import pandas as pd

import numpy as np

path = '秦皇岛试卷订单总表本.xls'

'''
获取所有表名称
'''


# 方法一
# io 获取文件路径
# sheet_name 要操作的表名
# header 取该行以下
def get_sheetnames(path):
    wb_sheet = pd.read_excel(io=path, sheet_name=None)
    print(wb_sheet.keys())


# 方法二
# 获取表格
def get_sheetnames2(path):
    wb = pd.ExcelFile(path)
    # 获取所有sheet 名称
    sheet_names = wb.sheet_names
    print(sheet_names)


'''
'''
df = pd.read_excel(io=path, sheet_name='青龙本')
print(df['试卷名称'].values)
# print(df['试卷名称'].unique())
# print(df.info())
# print(df.dtypes)
# print(df.isnull)
# print(df.values)
# print(df.columns)


