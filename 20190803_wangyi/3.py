import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    value = list(map(int, sys.stdin.readline().strip().split()))
    res = []
    if sum(value) % 2 != 0:
        value.sort()
        for each in value:
            res.append(str(each))
    else:
        even = False
        for i in range(len(value)):
            if value[i] % 2 == 0:
                even = True
        if even:
            value.sort()
            for each in value:
                res.append(str(each))
        else:
            for each in value:
                res.append(str(each))

    print(" ".join(res))
