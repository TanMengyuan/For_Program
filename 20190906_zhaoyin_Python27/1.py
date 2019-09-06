import sys

[n, k] = list(map(int, sys.stdin.readline().strip().split()))
value = list(map(int, sys.stdin.readline().strip().split()))
for _ in range(k - len(value)):
    value.append(0)
value.append(0)

tmp, days = 0, -1
for i in range(n):
    tmp += min(value[i], 8)
    value[i + 1] += max(0, value[i] - 8)
    if tmp >= k:
        days = i + 1
        break

print days
