"""
input:
a11b2c3
output:
aaaaaaaaaaabbccc
"""
s=(input())
i=0
while i<len(s):
  s1=''
  if(s[i].isnumeric()):
    j=i
    while j<len(s) and s[j].isdigit():
      s1+=s[j]
      j+=1 
    print(s[i-1]*int(s1),end='')
    i=j
  i+=1
