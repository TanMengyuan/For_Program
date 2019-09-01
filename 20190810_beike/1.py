def GetResult(K):
    n = 1
    while True:
        mutAll = 1
        for i in range(1, n + 1):
            mutAll *= i
        left = 0
        for i in range(1, n + 1):
            left += mutAll / i

        if left / mutAll > K:
            return n
        else:
            n += 1

print(GetResult(2))