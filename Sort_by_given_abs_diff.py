"""
input:
1 2 3 4 5
3
output:
3 2 4 1 5
explaination:
abs(3-1)=2
abs(3-2)
"""
lis = list(map(int, input().split()))
x = int(input())


def func(i):
    return abs(x - i)


lis.sort(key=func)
print(*lis, sep=" ")
