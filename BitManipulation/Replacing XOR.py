"""
input:
32 8 5 10
output:
32 8 1 11
"""
import math
from math import log,floor
def findXOR(n):
    mod = n % 4;
    if (mod == 0):
        return n;
    elif (mod == 1):
        return 1;
    elif (mod == 2):
        return n + 1;
    elif (mod == 3):
        return 0;

def findXORFun(l, r):
    return (findXOR(l - 1)^findXOR(r));

l=list(map(int,input().split()))
for i in range(len(l)):
  k=(floor(log(l[i],2)))
  k=2**k
  if k!=l[i]:
    l[i]=findXORFun(k,l[i])
print(*l)
