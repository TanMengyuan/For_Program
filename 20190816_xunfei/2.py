import sys

def findByBinarySearch(li, tar, left, right):
    if left > right:
        return
    mid = (left + right) // 2
    if li[mid] == tar:
        return mid
    elif target < li[mid]:
        return findByBinarySearch(li, tar, left, mid - 1)
    else:
        return findByBinarySearch(li, tar, mid + 1, right)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    target = int(sys.stdin.readline().strip())

    res = findByBinarySearch(values, target, 0, len(values))
    if not res and res != 0:
        print(-1)
    else:
        print(res)