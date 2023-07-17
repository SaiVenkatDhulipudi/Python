"""
input:
1 2 1 2 3 1
output:
3 2 2 1 1 1
"""
lis = list(map(int, input().split()))
print(sorted(lis, key=lis.count), sep=" ")
