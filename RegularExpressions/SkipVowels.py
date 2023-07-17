"""
input:
hello python
////////
output:
hll pythn
"""
import re

s = input()
s = re.sub("[aeiou]", "", s)
print(s)
