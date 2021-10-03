"""
Given the following three values, find the total number of maximum chocolates you can eat.
m: Money you have to buy chocolate 
p: Price of a each chocolate 
w: Number of wrappers to be returned for getting one extra chocolate.
s1:
16 2 2
15
"""
m,p,w=map(int,input("enter m,p,w: ").split())
k=m//p
x=k
while k>=w:
  x+=(k//w)
  k=(k%w)+(k//w)
print(x)
