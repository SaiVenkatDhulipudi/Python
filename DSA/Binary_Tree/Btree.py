class node:
    def __init__(self, x):
        self.data = x
        self.left = self.right = None


# creation
def create(root, lis, i, n):
    if i < n:
        root = node(lis[i])
        root.left = create(root.left, lis, 2 * i + 1, n)
        root.right = create(root.right, lis, 2 * i + 2, n)
    return root


# inorder
def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# main
if __name__ == "__main__":
    n = int(input())
    lis = list(map(int, input().split()))
    root = None
    root = create(root, lis, 0, n)
    inorder(root)
