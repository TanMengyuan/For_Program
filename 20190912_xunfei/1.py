import sys

m = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())


def solution(m, k):
    if m <= 0 or k < 0:
        return 0
    return m * k + cal_num(m, 0)


def cal_num(remain, num):
    if remain == 1:
        return num
    num += num + fac(remain - 1) + 1
    return cal_num(remain - 1, num)


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


if __name__ == '__main__':
    print(solution(m, k))
