import xlrd

path1 = 'byscj_ou本.xlsx'
path2 = '成绩单本.xlsx'

wb = xlrd.open_workbook(path1)
sheet1 = wb.sheet_by_name('sheet1')

ls1 = []
for i in range(11072):
    if sheet1.cell(i,0).value == '学号：':
        # print(sheet1.cell(i,2).value)
        ls1.append(sheet1.cell(i,2).value)

print(ls1)

wb = xlrd.open_workbook(path2)
sheet2 = wb.sheet_by_name('sheet1')

for i in range(11072):
    if sheet1.cell(i,0).value == '学号：':
        # print(sheet1.cell(i,2).value)
        if sheet1.cell(i,2).value not in ls1:
            print('sheet1.cell(i,2).value')