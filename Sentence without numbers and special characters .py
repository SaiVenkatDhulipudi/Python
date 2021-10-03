"""
input:
hey I am 13 now!
output:
Hey I am now
"""
s=str(input())
res=''
for i in s:
  if i==' 'or i.isalpha():
    res+=i
res=list(res.split())
res[0]=res[0].title()
res=' '.join(res)
print(res)
