"""
input:
abc apple monkey plea
abpcplea
output:
apple
"""
l=list(map(str,input().split()))
s=input()
d={}
ma=0
for i in l:
  c=0
  ind=0
  for j in i:
    if j in s[ind:]:
      c+=1
      ind=i.index(j)+1
    else:
      break
  d[i]=c
print(d)
k=max(d,key=d.get)
print(k)
