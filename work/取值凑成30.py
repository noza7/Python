'''
用于获取接近某个值的列表
'''


def ls_to_int(ls):
    '''
    将列表字符元素转换为整数并排序
    :param ls:需要转换的列表
    :return:转换后的列表
    '''
    ls = list(map(int, ls))
    ls = list(sorted(ls, reverse=True))
    return ls


def remove_ls(ls, ls_add):
    '''
    去除找到的元素
    :param ls: 原表
    :param ls_add: 原表中提取的一部分数值组成的新列表
    :return: 去除ls_add后的ls
    '''
    for i in range(len(ls_add)):
        remove_value = ls.index(ls_add[i])
        ls.pop(remove_value)
    return ls


def get_ls_equal_num(ls, num):
    '''
    获取一个列表中的一组数，让他们相加的结果接近于给定数
    :param ls: 列表
    :param num: 接近值
    :return: 排序在前的，并接近给定值的一组数列表
    '''
    ls_add = []
    x = 0
    for i in range(len(ls)):
        # print('-' * 30 + str(i))
        x = sum(ls_add)
        # print('x的当前值{}'.format(x))
        if x > num:
            ls_add.remove(ls[i - 1])
            # print('弹出的值{}'.format(ls[i - 1]))
        ls_add.append(ls[i])
        # print('加入当前的ls[i]值{}'.format(ls[i]))
    # 判断最后一个值
    if sum(ls_add) > num:
        ls_add.pop()
    return ls_add


ls = ['1', '30', '30', '30', '30', '1', '27', '23', '1', '17', '15', '11', '9', '7', '6', '2', '2', '2', '1', '1']

print(ls)


def get_all_close2num(ls):
    '''
    获取所有接近30的列表
    :param ls: 需要查找的列表
    :return: 所有接近值列表的列表
    '''
    ls = ls_to_int(ls)
    ls_ = []
    while len(ls) > 0:
        ls_add = get_ls_equal_num(ls, 30)
        # print(ls_add)
        ls_.append(ls_add)
        ls = remove_ls(ls, ls_add)
    return ls_


ls = get_all_close2num(ls)
print(ls)
