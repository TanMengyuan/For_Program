import sys

s = sys.stdin.readline().strip()


def solution(s):
    r = [[(j - k) * 9 % 13 for j in range(10)] for k in range(13)]
    d = [1] + [0] * 12
    mod = 10 ** 9 + 7
    for each in s:
        if each == '?':
            d = [sum(d[j] for j in k) % mod for k in r]
        else:
            d = [d[(int(each) - k) * 9 % 13] for k in range(13)]

    return d[5]


if __name__ == '__main__':
    print(solution(s))
