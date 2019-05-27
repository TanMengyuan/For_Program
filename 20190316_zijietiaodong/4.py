import sys

if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    nm = list(map(int, line.split()))
    n, m = nm[0], nm[1]
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))

    cut_num = m // n
    values.sort()
    sum_value = sum(values)

    minn = 0
    maxx = int(1e10 * (n / m))
    print(maxx)
    for mid in range(1, int(1e10)):
        mid /= 100
        c = 0
        for i in range(n):
            c += int(values[i] / mid)
        if c < m:
            minn = mid - 0.01
            break

    print(round(minn, 2))
