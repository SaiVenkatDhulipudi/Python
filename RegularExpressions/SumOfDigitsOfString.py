# problem link
"""https://practice.geeksforgeeks.org/problems/sum-of-numbers-in-string"""
import re

s = input()
lis = re.sub("[a-z]", " ", s.lower()).split()
add = 0
for i in lis:
    add += int(i)
print(add)
