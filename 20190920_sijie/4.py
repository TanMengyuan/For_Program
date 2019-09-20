"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/9/20 20:43
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxShared' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH friends as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

def maxShared(friends_nodes, friends_from, friends_to, friends_weight):
    # Write your code here
    dic = {}
    for i in range(len(friends_from)):
        a, b = friends_from[i], friends_to[i]
        if a > b:
            a, b = b, a
        tmp = str(a) + " " + str(b)
        if tmp in dic.keys():
            dic[tmp] += 1
        else:
            dic[tmp] = 1
    max_num = max(dic.values())
    sorted_dic = sorted(dic.items(), key=lambda x: x[1])
    res = 0
    for k, v in sorted_dic:
        if v == max_num:
            [a, b] = list(map(int, k.split()))
            res = max(res, a * b)
    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    friends_nodes, friends_edges = map(int, input().rstrip().split())

    friends_from = [0] * friends_edges
    friends_to = [0] * friends_edges
    friends_weight = [0] * friends_edges

    for i in range(friends_edges):
        friends_from[i], friends_to[i], friends_weight[i] = map(int, input().rstrip().split())

    result = maxShared(friends_nodes, friends_from, friends_to, friends_weight)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
