import re
s = '考场号：3009    人数：85'
p = '^考场号：(\d{4})'
r1 = re.findall(p, s)
print(r1)

str = "a123b"
print(re.findall(r"a(.+?)b",str))
