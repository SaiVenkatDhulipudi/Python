'''
input:
6
3 9 7 6 43 67
3
output:
116
'''
n=int(input())
l=list(map(int,input().split()))
k=int(input())
su=ma=sum(l[0:k])
j=0
for i in range(k,n):
  temp=su+l[i]-l[j]
  ma=max(temp,su)
  su=temp
  j+=1 
print(ma)
