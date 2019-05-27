import sys

# for line in sys.stdin:
#     a = int(line)

a = int(input())

r = 1024 - a
coin_64, r = r // 64, r % 64
coin_16, r = r // 16, r % 16
coin_4, r = r // 4, r % 4

print(coin_64 + coin_16 + coin_4 + r)