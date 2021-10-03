n=int(input())
l=list(map(int,input().strip().split()))
inf=10000000000
temp=[]
for i in range(n):
  mi=min(l)
  ind=l.index(mi)
  l[ind]=inf
  temp.append(mi)
print(*temp,sep=' ')
