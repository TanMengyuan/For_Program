s = list(input().split())

for i in range(len(s)):
    if len(s[i]) % 2 == 1:
        s[i] = s[i][::-1]

print(" ".join(s))