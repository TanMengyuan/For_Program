ss = '0abcdefgh1abcdefgh'

def func(n, s):
    dx, p, res = [], [], []
    for i in range(n):
        dx.append(s[i * 9])
        p.append(s[i * 9 + 1:(i + 1) * 9])
    for d in dx:
        tmp = p.pop(0)
        if d == '0':
            res.append(''.join(tmp[::-1]))
        else:
            res.append(''.join(tmp))

    return ' '.join(res)

print(func(2, ss))