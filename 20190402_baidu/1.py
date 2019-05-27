s = input()
li = []
for i in range(len(s)):
    s = s[1:] + s[0]
    if s not in li:
        li.append(s)

print(len(li))
