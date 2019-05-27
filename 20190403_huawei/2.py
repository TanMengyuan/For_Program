import sys
if __name__ == "__main__":
    data = []
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        data.append(line)

    legal, illegal, head = [], [], []
    for i in range(len(data)):
        Flag = True
        for each in data[i]:
            if '0' <= each <= '9' or 'a' <= each <= 'z' or 'A' <= each <= 'Z':
                continue
            else:
                Flag = False
        if Flag:
            if data[i] not in legal:
                legal.append(data[i])
        else:
            illegal.append(data[i])

    shift_ten = []
    for each in legal:
        shift_pos = 10 % len(each)
        shift_ten.append(each[shift_pos:] + each[:shift_pos])

    # print(' '.join(legal) + ' ' + ' '.join(illegal) + ' ' + ' '.join(shift_ten) + ' ' + ' '.join(sorted(shift_ten)))
    print(' '.join(legal))
    print(' '.join(illegal))
    print(' '.join(shift_ten))
    print(' '.join(sorted(shift_ten)))