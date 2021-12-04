def isminheap(l,n,i):
  
  if i>=int((n-2)/2):
    
    return True
  
  if l[i]<l[2*i+1] and l[i]<l[2*i+1] and isminheap(l,n,2*i+1) and isminheap(l,n,2*i+2):
    
    return True
  
  return False

if __name__=="__main__":
  n=int(input())
  l=list(map(int,input().split()))
  print(isminheap(l,n,0))

