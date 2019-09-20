"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
@time: 2019/9/20 19:55
"""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxPathSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY board
#  2. INTEGER p
#  3. INTEGER q
#

def maxPathSum(board, p, q):
    # Write your code here
    row = len(board)
    col = len(board[0])
    p_b = [[0 for _ in range(col)] for _ in range(row)]
    q_b = [[0 for _ in range(col)] for _ in range(row)]
    p_b[-1] = board[-1]
    for i in range(row - 2, -1, -1):
        for j in range(col):
            if j == 0:
                p_b[i][j] = max(p_b[i + 1][0], p_b[i + 1][1])
            elif j == col - 1:
                p_b[i][j] = max(p_b[i + 1][j - 1], p_b[i + 1][j])
            else:
                p_b[i][j] = max(p_b[i + 1][j - 1], p_b[i + 1][j], p_b[i + 1][j + 1])
            p_b[i][j] += board[i][j]
    q_b[0] = board[0]
    for i in range(1, row):
        for j in range(col):
            if j == 0:
                q_b[i][j] = max(q_b[i - 1][0], q_b[i - 1][1])
            elif j == col - 1:
                q_b[i][j] = max(q_b[i - 1][j - 1], q_b[i - 1][j])
            else:
                q_b[i][j] = max(q_b[i - 1][j - 1], q_b[i - 1][j], q_b[i - 1][j + 1])
            q_b[i][j] += board[i][j]
    return max(p_b[0][p], q_b[-1][q])


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    board_rows = int(input().strip())
    board_columns = int(input().strip())

    board = []

    for _ in range(board_rows):
        board.append(list(map(int, input().rstrip().split())))

    p = int(input().strip())

    q = int(input().strip())

    result = maxPathSum(board, p, q)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

    print(result)
