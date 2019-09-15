import sys

n = int(sys.stdin.readline().strip())
value = [[0 for _ in range(n)] for _ in range(n)]
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    [u, v, c] = list(map(int, line.strip().split()))
    value[u - 1][v - 1] = c


def find_sub_tree(num, conut):
    if any(value[num]):
        res = 0
        for i in range(len(value[num])):
            if value[num][i] != 0:
               res = max(res, find_sub_tree(i, value[num][i] + conut))
        return res
    else:
        return conut


def solution(n, value):
    res = [0 for _ in range(n)]
    for i in range(n):
        res[i] = find_sub_tree(i, 0)

    res = map(str, res)
    return " ".join(res)


if __name__ == '__main__':
    print(solution(n, value))

