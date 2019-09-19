"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
"""
import sys

s = sys.stdin.readline().strip()


def solution(s):
    ind_rl = []
    ori = [1 for _ in range(len(s))]
    for i in range(len(s)):
        if s[i] == "R" and s[i + 1] == "L":
            ind_rl.append(i)
    pre = 0
    for i in range(len(ind_rl)):
        for j in range(pre, ind_rl[i]):
            if s[j] == "R":
                if (ind_rl[i] - j) % 2 == 0:
                    ori[ind_rl[i]] += 1
                else:
                    ori[ind_rl[i] + 1] += 1
            else:
                if ((j - ind_rl[i - 1]) % 2) == 0:
                    ori[ind_rl[i - 1]] += 1
                else:
                    ori[ind_rl[i - 1] + 1] += 1
            ori[j] -= 1
        pre = ind_rl[i] + 2

    ori = map(str, ori)

    return " ".join(ori)


if __name__ == '__main__':
    print(solution(s))