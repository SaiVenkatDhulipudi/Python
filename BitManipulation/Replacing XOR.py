"""
input:
32 8 5 10
output:
32 8 1 11
"""
from math import floor, log


def findXOR(n):
    mod = n % 4
    if mod == 0:
        return n
    elif mod == 1:
        return 1
    elif mod == 2:
        return n + 1
    elif mod == 3:
        return 0


def findXORFun(left, r):
    return findXOR(left - 1) ^ findXOR(r)


lis = list(map(int, input().split()))
for i in range(len(lis)):
    k = floor(log(lis[i], 2))
    k = 2**k
    if k != lis[i]:
        lis[i] = findXORFun(k, lis[i])
print(*lis)
