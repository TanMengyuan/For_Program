# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    values = []
    for i in range(n * 2):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        if i % 2 == 0:
            values.append(int(line))
        else:
            values.append(list(map(int, line.split())))

    p = values[::2]
    score = values[1::2]

    for i in range(n):
        gifts = [1 for _ in range(p[i])]
        for j in range(p[i]):
            if score[i][j] > score[i][j - 1]:
                gifts[j] = gifts[j - 1] + 1

        for j in reversed(range(p[i])):
            if score[i][j - 1] > score[i][j] and gifts[j - 1] <= gifts[j]:
                gifts[j - 1] = gifts[j] + 1

        print(sum(gifts))