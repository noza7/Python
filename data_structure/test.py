data = [{'10': {'张三': {'数学': '10', '英语': '20', '体育': '30'}}}, {'20': {'李四': {'数学': '10', '英语': '20', '体育': '30'}}}]
# todo 取第一个学生
student = data[0]
# print(student)
# todo 取学号
student_num = list(student.keys())[0]
print(student_num)
# todo 姓名
# student_name = list(list(student.values())[0].keys())[0]
student_name = list(student[student_num])[0]
print(student_name)
# todo 成绩
student_scores = list(student[student_num].values())[0]
print(student_scores)
