import sys

if __name__ == "__main__":
    # n = int(sys.stdin.readline().strip())
    # li = []
    # for _ in range(n):
    #     li.append(list(map(int, sys.stdin.readline().strip().split())))

    n = 4
    li = [[4, 7], [2, 6], [2, 5], [1, 2]]
    li = [[1, 1], [1, 3]]
    li.sort()
    max_i = max(max(li))
    min_i = min(min(li))
    sta = [0 for _ in range(max_i - min_i + 2)]
    for s, e in li:
        sta[s - min_i] += 1
        sta[e - min_i + 1] -= 1
    res, max_r = 0, 0
    print(sta)
    for num in sta:
        res += num
        if res > max_r:
            max_r = res
    print(max_r)