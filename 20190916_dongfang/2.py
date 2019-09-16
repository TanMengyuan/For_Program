import sys

s = sys.stdin.readline().strip()
try:
    print(eval(s))
except:
    print(-1)
