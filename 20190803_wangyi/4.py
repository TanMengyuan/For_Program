import sys
if __name__ == "__main__":
    li = list(map(int, sys.stdin.readline().strip().split()))
    m, n = li[0], li[1]
    value = list(map(int, sys.stdin.readline().strip().split()))
    res = []
    for i in range(n):
        v = int(sys.stdin.readline().strip())
        count = 0
        for j in range(m):
            if value[j] >= v:
                value[j] -= 1
                count += 1
        res.append(count)
    for each in res:
        print(each)