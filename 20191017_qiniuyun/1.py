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
    map = {}
    flag = True
    for i in range(arr_len):
        if arr[i] not in map:
            map[target - arr[i]] = i
        else:
            print(map[arr[i]], i)
            flag = False

    if flag:
        print(-1, -1)