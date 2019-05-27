def string(string):
    str1 = list(string)
    set = []
    for x in str1:
        set.append(x)
        length = len(set)
        if length > 2:
            if set[length - 1] == set[length - 2] and set[length - 1] == set[length - 3]:
                set.pop()
            length = len(set)
            if length > 3:
                if set[length - 1] == set[length - 2] and set[length - 3] == set[length - 4]:
                    set.pop()
    str = ''.join(set)
    return str


import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    values = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values.append(line)

    for i in range(n):
        print(string(values[i]))