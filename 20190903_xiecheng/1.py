import sys

n = int(sys.stdin.readline().strip())
li = [1, 1]

for i in range(n - 2):
    li.append(li[i] + li[i + 1])

print(li[-1])