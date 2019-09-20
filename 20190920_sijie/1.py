"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/9/20 19:07
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'betterCompression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def betterCompression(s):
    dic = {}
    tmp = 0
    cur_char = ""
    for e in s:
        if "a" <= e <= "z":
            if tmp != 0:
                if cur_char in dic.keys():
                    dic[cur_char] += tmp
                else:
                    dic[cur_char] = tmp
                tmp = 0
            cur_char = e
        else:
            tmp = 10 * tmp + int(e)
    if tmp != 0:
        if cur_char in dic.keys():
            dic[cur_char] += tmp
        else:
            dic[cur_char] = tmp
    sort_dic = sorted(dic.items(), key=lambda x: x[0])
    res = ""
    for k, v in sort_dic:
        res += str(k) + str(v)

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = betterCompression(s)

    fptr.write(result + '\n')

    fptr.close()
