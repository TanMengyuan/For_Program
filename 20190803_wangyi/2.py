import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    res = []
    for i in range(n):
        m = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        if m <= 2:
            res.append("NO")
            break
        value = list(map(int, line.split()))
        flag = True
        for j in range(m):
            if value[j] > value[j - 1] + value[(j + 1) % m]:
                flag = False
        if flag:
            res.append("YES")
        else:
            res.append("NO")
    for each in res:
        print(each)