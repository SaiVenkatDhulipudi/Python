"""
input:
6
10 10 10 20 20 30
output:
10-3
20-2
30-1
"""
from collections import OrderedDict
n=int(input())
l=list(map(int,input().split()))
dic={}
for i in l:
  if i not in dic:
    dic[i]=1
  else:
    dic[i]+=1
dic=OrderedDict(sorted(dic.items()))
for key in dic:
  print('%s-%s'%(key,dic[key]))
