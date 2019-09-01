import sys

s = sys.stdin.readline().strip()


def max_sub_string(string):
    dic = {}
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i:j] in dic.keys():
                dic[string[i:j]] += 1
            else:
                dic[string[i:j]] = 1
    return max(dic.values())


if __name__ == "__main__":
    print(max_sub_string(s))