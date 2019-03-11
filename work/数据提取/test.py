import pandas as pd
path = 'table.xlsx'
df = pd.read_excel(io=path, sheet_name=0, index_col='学号')
# 取表头，转化为列表
title = df.columns.tolist()
# 取一行数据，转化为列表
data = df.loc[1313001456612, :].astype(str).tolist()
# 取姓名，转化为列表
name = df.loc[1313001456612, ['姓名']].astype(str).tolist()
# 取索引，转化为列表
index = df.index.tolist()
# 打包成字典
# 数据结构 [['1601313030001', ['郭子铭', {'工程造价实训': '50', '数学': '30'}]], ['1601313030002', ...]]
data_dict = dict(zip(title, data))
# 生成数据列表
all = []
for i in index:
    ls = []
    student_data = df.loc[i, :].astype(str).tolist()
    # 打包成字典
    student_dict = dict(zip(title, student_data))
    student_name = df.loc[i, ['姓名']].tolist()
    student_name.append(student_dict)
    ls.append(str(i))
    ls.append(student_dict)
    all.append(ls)

print(all)
