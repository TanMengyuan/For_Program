import sys

n = int(sys.stdin.readline().strip())
v = []
for i in range(2):
    v.append(list(map(int, sys.stdin.readline().strip().split())))

[ai, bi] = [v[0], v[1]]
all_ai = sum(ai)
rank_bi = sorted(bi, reverse=True)

