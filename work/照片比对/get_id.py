import os
import openpyxl


def get_file_name(file_dir):
    '''
    获取指定目录下所有文件名称
    :param file_dir:指定目录
    :return:返回文件名列表
    '''
    for root, dirs, files in os.walk(file_dir):
        # return root#当前目录路径
        # return dirs#当前路径下所有子目录
        return files  # 当前路径下所有非目录子文件


def class_file_name(file_dir, file_type):
    '''
    获取指定文件夹下的指定文件类型名称
    :param file_dir:指定目录
    :param file_type:
    :return:返回文件名列表
    '''
    ls = []
    f = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == file_type:
                ls.append(os.path.join(root, file))
                f.append(file)
    return f


def output2excel(file_dir):
    '''
    把文件夹下的文件名称输出到文件目录
    :param file_dir: 文件目录
    :return:
    '''
    # 获取文件目录下所有文件名，存入data列表
    data = get_file_name(file_dir)

    # 把data输出到该目录下，并以目录名保存为excel格式
    wb = openpyxl.Workbook()
    sheet = wb.active
    # 设置表名为文件目录名
    sheet.title = file_dir
    for i in range(1, len(data) + 1):
        sheet['A{}'.format(i)] = data[i - 1]

    if file_dir == '':
        file_dir = '当前目录'
    wb.save('{0}/{0}.xlsx'.format(file_dir))


file_dir = '本科'
output2excel(file_dir)
