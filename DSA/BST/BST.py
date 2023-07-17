class node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


# creating BST
def create(root, x):
    if root is None:
        return node(x)
    elif x > root.data:
        root.right = create(root.right, x)
    else:
        root.left = create(root.left, x)
    return root


# inorder
def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# postorder
def postorder(root):
    if root is None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# preorder


def preorder(root):
    if root is None:
        return
    else:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


if __name__ == "__main__":
    n = int(input())
    lis = list(map(int, input().split()))
    root = None
    for i in lis:
        root = create(root, i)
    print("Inorder:", end="")
    inorder(root)
    print()
    print("Postorder:", end="")
    postorder(root)
    print()
    print("Preorder:", end="")
    preorder(root)
