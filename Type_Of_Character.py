"""
input:
a
output:
alphabet
input:
1
output:
number
input:
a1
output:
alpha numeric
"""
s=str(input())
if s.isalpha():
  print("alphabet")
elif s.isnumeric():
  print("number")
elif s.isalnum():
  print("alpha numeric")
