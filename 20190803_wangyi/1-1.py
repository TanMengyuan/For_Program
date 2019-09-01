import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    score = list(map(int, sys.stdin.readline().strip().split()))
    times = int(sys.stdin.readline().strip())
    res = []
    for i in range(times):
        stuIdx = int(sys.stdin.readline().strip()) - 1
        res.append("%.6f" % ((100 * (sum(i <= score[stuIdx] for i in score) - 1)) / n))
    for each in res:
        print(each)