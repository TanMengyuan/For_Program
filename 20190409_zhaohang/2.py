import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    if n < 6:
        print(0)
    else:
        count = 1
        for i in range(n - 6):
            count += 2 ** i
        print(count)
