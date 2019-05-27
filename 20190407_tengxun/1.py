import sys

data = list(map(int, sys.stdin.readline().strip().split()))
N = [data[0]]
K = data[1]
ans = 0


def Split(N):
    lis = []
    for each in N:
        if each // 2 != 0:
            lis.append(each // 2)
        if each - each // 2:
            lis.append(each - each // 2)
    return lis


def is_zero(x): return x != 0


def subtract(x): return x - 1


while N:
    while max(N) >= 4 and K > 0:
        N = Split(N)
        K -= 1
        ans += 1
    N = list(map(subtract, N))
    N = list(filter(is_zero, N))
    ans += 1

print(ans)