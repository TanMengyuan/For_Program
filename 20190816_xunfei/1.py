import sys
for line in sys.stdin:
    n = int(line)

def maxNum(x):
    if x == 2:
        return 2
    if x == 3:
        return 3
    if x < 2:
        return 0
    if x == 4:
        return 4

    return 3 * maxNum(x - 3)

print(maxNum(n))