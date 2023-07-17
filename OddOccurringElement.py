lis = list(map(int, input().split()))
c = 0
for i in lis:
    c ^= i
print(c)
