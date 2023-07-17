n = int(input())
lis = list(map(int, input().strip().split()))
inf = 10000000000
temp = []
for i in range(n):
    mi = min(lis)
    ind = lis.index(mi)
    lis[ind] = inf
    temp.append(mi)
print(*temp, sep=" ")
