"""
input:
1 2 1 2 3 1
output:
3 2 2 1 1 1
"""
l=list(map(int,input().split()))
l1=sorted(l,key=l.count)
print(*l1,sep=' ')
