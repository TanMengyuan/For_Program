def pushDominoes(dominoes: str):
    dom = list(dominoes)
    if len(dominoes) <= 1:
        return dominoes
    state = "."
    lastpos = 0
    for i in range(0,len(dom)):
        if dom[i] == '.':
            if i == len(dom)-1 and state =="R":
                for j in range(lastpos,i+1):
                    dom[j] ='R'
            else:
                continue
        elif dom[i] == 'L':
            if state ==".":
                for j in range(lastpos,i):
                    dom[j] = 'L'
            elif state =="R":
                if (lastpos+i)%2 == 0:
                    mid = (lastpos+i) // 2
                    for j in range(lastpos, mid):
                        dom[j] = 'R'
                    for j in range(mid+1, i):
                        dom[j] = 'L'
                else:
                    mid = (lastpos + i) // 2 + 1
                    for j in range(lastpos, mid):
                        dom[j] = 'R'
                    for j in range(mid, i):
                        dom[j] = 'L'
            elif state == "L":
                for j in range(lastpos, i):
                    dom[j] = 'L'
            else:
                pass
            state = "L"
            lastpos = i
        elif dom[i] == 'R':
            if state == ".":
                pass
            elif state == "L":
                pass
            elif state == "R":
                for j in range(lastpos, i):
                    dom[j] = 'R'
            else:
                pass
            state = "R"
            lastpos = i
        else:
            pass

    r = "".join(dom)
    return r

print(pushDominoes(input()))