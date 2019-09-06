import sys


def bag(s, m, w, v):
    res = [[-1 for _ in range(m + 1)] for _ in range(s + 1)]

    for j in range(m + 1):
        res[0][j] = 0

    for i in range(1, s + 1):
        for j in range(1, m + 1):
            res[i][j] = res[i - 1][j]
            if j >= w[i - 1] and res[i][j] < res[i - 1][j - w[i - 1]] + v[i - 1]:
                res[i][j] = res[i - 1][j - w[i - 1]] + v[i - 1]

    print(res[s][m])


if __name__ == '__main__':
    [s, m] = list(map(int, sys.stdin.readline().strip().split()))
    w, v = [], []
    for i in range(s):
        [wi, vi] = list(map(int, sys.stdin.readline().strip().split()))
        w.append(wi)
        v.append(vi)

    bag(s, m, w, v)
