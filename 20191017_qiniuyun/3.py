"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
"""
import sys

arr_len = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
target = int(sys.stdin.readline().strip())

if __name__ == '__main__':
    left, right = 0, arr_len - 1
    while left < right:
        if arr[left] != target:
            left += 1
        if arr[right] != target:
            right -= 1
        if arr[left] == target and arr[right] == target:
            break
    if arr[left] != target:
        print(-1, -1)
    else:
        print(left, right)

