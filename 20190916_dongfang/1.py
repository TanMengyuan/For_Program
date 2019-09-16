import sys

arr1 = list(map(int, sys.stdin.readline().strip().split(",")))
arr2 = list(map(int, sys.stdin.readline().strip().split(",")))

res = []
for a in arr1:
    for b in arr2:
        res.append(a + b)

res = list(map(str, sorted(set(res))[:3]))
if "1" in res:
    print(",".join(res))
