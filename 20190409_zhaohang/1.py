import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    li = []
    for i in range(n):
        li.append(int(sys.stdin.readline().strip()))

    p = sum(li)
    max_p = max(li)
    if m <= n * max_p - p:
        k_min = max_p
    else:
        k_min = ((m - (n * max_p - p)) // n) + 1 + max_p
    k_max = max_p + m

    print(k_min, k_max)
