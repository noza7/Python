# -!- coding: utf-8 -!-

from itertools import combinations, permutations

'''
search all combinations like 123-45-67+89 = 100
'''


def tri_add(operators):
    # 三进制加1算法，以8个元素为例
    # 列表中的数字从[0,0,0,0,0,0,0,0,]变到[3,3,3,3,3,3,3,3,]
    lastPosition = len(operators) - 1
    c = 1
    for i in range(lastPosition, -1, -1):
        c, operators[i] = divmod(operators[i] + c, 3)
        if c == 0:
            return None
    # 如果循环结束时c的值为1
    # 表示列表已经变到[3,3,3,3,3,3,3,3,]，不再允许变化
    return 1


def combination_high(digits='123456789', total=48):
    # 分别在1到9之间的数字之间插入空格、+或-
    d = ' +-'
    operators = [0] * (len(digits) - 1)
    # print(operators)
    while not tri_add(operators):
        # 对于三进制的数字列表operators
        # 其中数字0对应空格，1对应+,2对d应-
        # 下面map后的值是一个对象
        # 要查看对象值需要使用list
        operators_out = list(map(lambda o: d[o], operators))
        # print(operators_out)
        expression = ''.join((o + c for o, c in zip(digits, operators_out))) + digits[-1]
        # print(expression)
        # 删除表达式中的空格
        expression = ''.join(expression.split())
        # print(expression)

        if eval(str(expression)) == total:
            print(expression)


combination_high()
