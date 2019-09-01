n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))

now = 1
count = 0
for i in range(n - 1):
    if now == 1:
        other = 0
    else:
        other = 1
    planA = li[i][now] + li[i + 1][now]
    planB = li[i][2] + li[i][other] + li[i + 1][other]
    res = min(planA, planB)
    if res == planA:
        count += li[i][now]
    else:
        count += li[i][other] + li[i][2]
        now = other

if now == 1:
    other = 0
else:
    other = 1
last = min(li[-1][now], li[-1][other] + li[-1][2])
count += last
print(count)