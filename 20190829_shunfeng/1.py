import sys

_ = sys.stdin.readline().strip()
passedSub = sys.stdin.readline().strip()
score = list(map(int, sys.stdin.readline().strip().split()))

passed = []
for e in passedSub:
    score[ord(e) - ord("A")] = -1


print(chr(score.index(max(score)) + ord("A")))

