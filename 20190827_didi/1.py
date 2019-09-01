
n = int(input())
v = list(input().split(" "))
value = [int(v[0])]
symbol = []

for i in range(1, n):
    value.append(int(v[2 * i]))
    symbol.append(v[2 * i - 1])

symbol.append("+")
print(value)
print(symbol)

# index = 0
# while index < n:
