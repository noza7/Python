list1 = ['key1', 'key2', 'key3']
list2 = ['1', '2', '3']
list3 = ['10', '20', '30']
list4 = []
for i in range(len(list2)):
    x = str(list2[i - 1]) + ':' + str(list3[i - 1])
    list4.append(x)

print(list4)
dict_ls = dict(zip(list1, list4))

print(dict_ls)
