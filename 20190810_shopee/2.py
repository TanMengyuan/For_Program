import sys
if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    minus = False
    if s[0] == "-":
        minus = True
        s = s[1:]
    out = s[::-1]
    out = int(out)
    if minus:
        out = -out
    if - sys.maxsize < out < sys.maxsize - 1:
        print(0)
    else:
        print(out)