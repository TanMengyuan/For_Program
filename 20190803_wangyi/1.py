import sys
import copy
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    score = list(map(int, sys.stdin.readline().strip().split()))
    temp = copy.deepcopy(score)
    temp.sort()
    times = int(sys.stdin.readline().strip())
    res = []
    for i in range(times):
        stuIdx = int(sys.stdin.readline().strip()) - 1
        k = 0
        for j in score:
            if j <= score[stuIdx]:
                k += 1
            else:
                break
        res.append("%.6f" % ((k - 1) / n))
    for each in res:
        print(each)