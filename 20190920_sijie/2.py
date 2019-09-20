"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/9/20 19:25
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMinimumMoves(arr):
    # Write your code here
    dummy = sorted(arr)
    count = 0
    idx = 0
    for i in range(len(arr)):
        if dummy[idx] == arr[i]:
            idx += 1
            count += 1
    return len(arr) - count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMinimumMoves(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
