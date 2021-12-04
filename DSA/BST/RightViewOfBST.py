class node:
  def __init__(self,x):
    self.data=x
    self.left=self.right=None
#creation
def create(root,x):
  if(root==None):
    return node(x)
  elif root.data>x:
    root.left=create(root.left,x)
  else:
    root.right=create(root.right,x)
  return root
#rightview
def rightview(root):
  if(root==None):
    return 
  else:
    l=[]
    l.append(root)
    while(len(l)!=0):
      n=len(l)
      while(n>0):
        x=l[0]
        l.pop(0)
        if(n==1):
          print(x.data,end=' ')
        if(x.left!=None):
          l.append(x.left)
        if(x.right!=None):
          l.append(x.right)
        n-=1
if __name__=="__main__":
  n=int(input())
  l=list(map(int,input().split()))
  root=None
  for i in l:
    root=create(root,i)
  rightview(root)

