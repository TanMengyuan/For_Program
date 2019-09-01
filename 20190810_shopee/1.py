import sys
import copy
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    li = []
    for i in range(n):
        sys.stdin.readline()
        tmp = 0
        for j in list(map(int, sys.stdin.readline().strip().split())):
            tmp += 1 << j
        li.append(tmp)
    score = [0 for _ in range(n)]
    sys.stdin.readline()
    # req = list(map(int, sys.stdin.readline().strip().split()))
    req = 0
    for j in list(map(int, sys.stdin.readline().strip().split())):
        req += 1 << j
    for i in range(n):
        li[i] = li[i] & req
    maxScore = 0
    for i in li:
        maxScore = max(bin(i).count("1"), maxScore)
    for i in range(len(li)):
        if bin(i).count("1") == maxScore:
            print(i + 1)