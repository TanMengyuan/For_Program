"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
"""
import sys

li = []
tmp = sys.stdin.readline().strip()
while tmp:
    li.append(tmp)
    tmp = sys.stdin.readline().strip()

res = []
for i in range(len(li)):
    sub = ""
    for e in li[i]:
        if e not in sub:
            sub += e
    res.append(sub)

for e in res:
    print(e)
