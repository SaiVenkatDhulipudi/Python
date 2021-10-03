n=int(input("enter size of list"))
l=list(map(int,input('enter list').strip().split()))
key=int(input('enter key'))
def binary_search(l,low,high,k):
  while low<=high:
    mid=(low+high)//2
    if l[mid]==k:
      return mid
    elif l[mid]>k:
      high=mid-1
    elif l[mid]<k:
      low=mid+1 
  return -1;
print(f'index= {binary_search(sorted(l),0,n-1,key)}') 
