import re

s = input()
dic = {}

li = re.findall("\d+", s)
for each in li:
    if each in dic.keys():
        dic[each] += 1
    else:
        dic[each] = 1

print(max(dic.items(),key=lambda x:x[1])[0])