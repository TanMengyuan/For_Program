import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    x = list(map(int, sys.stdin.readline().strip().split()))
    N = 10 ** 5
    count = [0 for _ in range(N)]
    ans = [0 for _ in range(N)]

    def convert(n, step):
        i = n
        while i < N:
            count[i] += 1
            ans[i] += step
            i *= 2
            step += 1

    res = 0
    for i in range(n):
        convert(x[i], 0)
        step = 0
        while x[i] // 2 > 0:
            if x[i] % 2 == 1:
                step += 1
                convert(x[i] // 2, step)
            else:
                ind = int(x[i] / 2)
                count[ind] += 1
                step += 1
                ans[ind] += step
            x[i] = x[i] // 2
        step += 1
        res += step
    for i in range(N):
        if count[i] == n:
            res = min(res, ans[i])

    print(res)