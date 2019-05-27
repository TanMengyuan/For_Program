import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    data = []
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        tmp = list(map(int, line.split(',')))
        data.append(tmp)

    print(data)

    # n = 4
    # data = [['2', '5', '6', '7', '9', '5', '7'], ['1', '7', '4', '3', '4']]
    li = [[] for _ in range(len(data))]
    m = len(data)
    max_len = 0
    for i in range(len(data)):
        if len(data[i]) > max_len:
            max_len = len(data[i])
        for j in range(0, len(data[i]), n):
            li[i].append(data[i][j: j + n])
    res = []
    for i in range(max_len):
        for j in range(len(data)):
            if len(li[j]) > i:
                res += li[j][i]

    # print(res)
    print(','.join(res))
