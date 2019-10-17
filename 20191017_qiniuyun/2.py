"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
"""
import sys

s = sys.stdin.readline().strip()


def solution(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    for i, v in enumerate(s):
        if v == '(' or v == '{' or v == '[' or v == '<':
            stack.append(v)
        elif len(stack) == 0:
            pass
        elif (v == ')' and stack[-1] == '(') or (v == ']' and stack[-1] == '[') or \
                (v == '}' and stack[-1] == '{') or (v == '>' and stack[-1] == '<'):
            stack.pop()
    return not stack


if __name__ == '__main__':
    print(1 if solution(s) else 0)
