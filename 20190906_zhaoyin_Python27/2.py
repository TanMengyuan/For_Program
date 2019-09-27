import sys

n = int(sys.stdin.readline().strip())
value = list(map(int, sys.stdin.readline().strip().split()))
value = sorted(value)[::-1]

pair = []
i = 0
while i < n - 1:
    if value[i] - value[i + 1] <= 1:
        pair.append(value[i + 1])
        i += 2
    else:
        i += 1

area = 0
for i in range(len(pair) / 2):
    area += pair[2 * i] * pair[2 * i + 1]

# print area
