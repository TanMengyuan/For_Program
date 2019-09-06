import sys

[n, m] = sys.stdin.readline().strip().split()
li = list(map(int, n))
m = int(m)
k = len(li) - m

start, end = 0, m
index = 0
max_value = -1
res = ""

for i in range(k):
    for j in range(start, end + 1):
        num = li[j]
        if num > max_value:
            max_value = num
            index = j
    res += str(max_value)
    max_value = -1
    start = index + 1
    end += 1

print(res)
