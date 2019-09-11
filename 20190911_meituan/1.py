"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/9/11 16:00
"""
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def findMaxSubListLen(a, b):
    len_a = len(a)
    len_b = len(b)
    dp = [[0 for _ in range(len_b + 1)] for _ in range(len_a + 1)]

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

    return max(max(each) for each in dp)


# ******************************结束写代码******************************


_a_cnt = 0
_a_cnt = int(input())
_a_i = 0
_a = []
while _a_i < _a_cnt:
    _a_item = int(input())
    _a.append(_a_item)
    _a_i += 1
# _a = list(map(int, input().strip().split()))

_b_cnt = 0
_b_cnt = int(input())
_b_i = 0
_b = []
while _b_i < _b_cnt:
    _b_item = int(input())
    _b.append(_b_item)
    _b_i += 1
# _b = list(map(int, input().strip().split()))

res = findMaxSubListLen(_a, _b)

print(str(res) + "\n")
