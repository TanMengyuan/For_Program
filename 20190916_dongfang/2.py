"""
@version: python3.7
@author: ‘mengyuantan‘
@contact: tanmy1016@126.com
"""
import sys

s = sys.stdin.readline().strip()
try:
    print(eval(s))
except:
    print(-1)
