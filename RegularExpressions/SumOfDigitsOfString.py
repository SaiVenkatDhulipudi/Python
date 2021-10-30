#problem link
https://practice.geeksforgeeks.org/problems/sum-of-numbers-in-string
import re
s=input()
l=(re.sub('[a-z]',' ',s.lower()))
l=l.split()
add=0
for i in l:
  add+=int(i)
print(add)
