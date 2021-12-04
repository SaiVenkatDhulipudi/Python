class node:
  def __init__(self,x):
    self.data=x
    self.right=self.left=None

def create(root,i,n,l):
  if(i<n):
    root=node(l[i])
    root.left=create(root.left,2*i+1,n,l)
    root.right=create(root.right,2*i+2,n,l)
  return root
def inorder(root):
  if root==None:
    return
  else:
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)
def mirror(root):
  if root==None:
    return
  else:
    mirror(root.right)
    print(root.data,end=' ')
    mirror(root.left)

if __name__=="__main__":
  n=int(input())
  l=list(map(int,input().split()))
  root=node(None)
  root=create(root,0,n,l)
  inorder(root)
  print()
  mirror(root)

