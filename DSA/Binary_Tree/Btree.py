class node:
  def __init__(self,x):
    self.data=x
    self.left=self.right=None
#creation
def create(root,l,i,n):
  if(i<n):
    root=node(l[i])
    root.left=create(root.left,l,2*i+1,n)
    root.right=create(root.right,l,2*i+2,n)
  return root
#inorder
def inorder(root):
  if root==None:
    return 
  else:
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)
#main
if __name__=='__main__':
  n=int(input())
  l=list(map(int,input().split()))
  root=None
  root=create(root,l,0,n)
  inorder(root)
