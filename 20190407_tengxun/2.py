import sys

if __name__ == "__main__":
    # 读取第一行的n
    # n = int(sys.stdin.readline().strip())
    # data = list(map(int, sys.stdin.readline().strip().split()))

    n = 5
    data = [5, -4, 1, -3, 1]

    carry = 0
    cost = 0

    for i in range(n):
        cost += abs(carry)
        carry += data[i]

    print(cost)