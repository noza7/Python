ls = ['123', '456.0']

a = str(ls[1]).split('.')
print(a)
data = a[0].zfill(5)
print(data)

b = str(int(float(ls[1])))
b = b.zfill(5)
print(b)




