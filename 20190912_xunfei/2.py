import sys

s = sys.stdin.readline().strip().split(",")


def solution(s):
    res = 0
    for each in s:
        if len(each) <= 1:
            continue
        tmp = 0
        for e in each:
            if "0" <= e <= "9":
                tmp += int(e)
            else:
                tmp = 0
                break
        if tmp > 8:
            res += 1
    return res


if __name__ == '__main__':
    print(solution(s))