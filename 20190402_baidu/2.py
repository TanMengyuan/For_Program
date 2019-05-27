# s = input()
# sub_s = input()
# n = int(input())
# r_li = []
# for i in range(n):
#     r_li.append(list(map(int, input().split())))

s = 'comeonmandontconconnect'
sub_s = 'on'
n = 5
r_li = [[1, 5], [1, 6], [1, 23], [11, 16], [11, 23]]
import re
ind = [i.start() for i in re.finditer(sub_s, s)]
print(ind)

for i in range(n):

    new = s[r_li[i][0] - 1: r_li[i][1]]
    print(new.count(sub_s))