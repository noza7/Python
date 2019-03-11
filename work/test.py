import xlrd

wb = xlrd.open_workbook('秦皇岛试卷订单总表本.xls')

sheet3 = wb.sheet_by_index(2)

cols = sheet3.ncols

for i in range(cols):
    if sheet3.cell_value(0, i) == '试卷名称':
        # print(sheet3.cell_value(0, i))
        print(sheet3.col_values(i))

# print(cols)