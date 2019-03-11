import pandas as pd
import time

start_time = time.time()
'''
利用pandas筛选并写入数据；
首先需要从数据表读入数据；

操作步骤：
去除学号重复的行，这样保留学生的唯一值；
筛选出16界之前的学生；
筛选出需要的列；
拆分开专科、本科；
分别统计班主任出现的次数；
'''
path = '生成数据.xlsx'

df = pd.read_excel(io=path, sheet_name='生成数据')
# print(df)

# 去除重复的行，也就是保留唯一学号
# 因为删除是在原表上做了改动，所以这样的操作最好做在前面，否则可能会出现警告
df.drop_duplicates(subset='学号', keep='first', inplace=True)

# 16界之前
df = df.astype(str)
# "^\d"以数字开始，"{1}"一位(因为学号可能会出现0或1)，"[0-5]"数字“0-5”（6之前的），".*?"后面随意
re = '^\d{1}[0-5].*?'
# 根据条件筛选出学号列
df_before_16 = df['学号'].str.contains(re, na=False)
# 补充符合条件的列
df_before_16 = df[df_before_16]
# 删除列
# df_before_16.drop(['ID', '姓名'], axis=1, inplace=True)

# 筛选出需要的列
df_new = df_before_16[['学号', '姓名', '班主任', '专本']]

# 筛选专本
df_zhuan = df_new[df_new['专本'].str.contains('专', na=False)]
df_ben = df_new[df_new['专本'].str.contains('本', na=False)]

# 统计班主任出现次数
df_zhuan_count = df_zhuan.groupby(['班主任'], as_index=False)['班主任'].agg({'出现次数': 'count'})
df_ben_count = df_ben.groupby(['班主任'], as_index=False)['班主任'].agg({'出现次数': 'count'})

# 创建新表
path_result = 'result.xlsx'
# 写入数据
writer = pd.ExcelWriter(path_result)
df_zhuan_count.to_excel(writer, '专')
df_ben_count.to_excel(writer, '本')
writer.save()
print('程序顺利执行完成！')

end_time = time.time()
print('用时：{0}秒'.format(end_time - start_time))
