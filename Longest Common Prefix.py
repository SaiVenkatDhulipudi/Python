"""
QUESTION LINK:
https://www.geeksforgeeks.org/longest-common-prefix-using-character-by-character-matching/
"""
n = int(input())
lis = list(map(str, input().split()))


def prefix():
    s = ""
    sub = min(lis)
    for i in range(len(sub)):
        for j in range(0, n):
            if sub[i] not in lis[j][i]:
                return s
        else:
            s += sub[i]
    return s


print(prefix())
