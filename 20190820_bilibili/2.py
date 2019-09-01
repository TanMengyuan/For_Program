import sys

[h, w] = list(map(int, sys.stdin.readline().strip().split()))
pic = []
for i in range(h):
    pic.append(list(map(int, sys.stdin.readline().strip().split())))
m = int(sys.stdin.readline().strip())
core = []
for i in range(m):
    core.append(list(map(float, sys.stdin.readline().strip().split())))

res = [[0 for _ in range(w - m + 1)] for _ in range(h - m + 1)]

for i in range(h - m + 1):
    for j in range(w - m + 1):
        tmp = 0
        for x in range(m):
            for y in range(m):
                tmp += pic[i + x][j + y] * core[x][y]
        res[i][j] = min(int(tmp), 255)

for each in res:
    print(" ".join(str(e) for e in each))