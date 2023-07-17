class node:
    def __init__(self, x):
        self.data = x
        self.right = self.left = None


def create(root, i, n, lis):
    if i < n:
        root = node(lis[i])
        root.left = create(root.left, 2 * i + 1, n, lis)
        root.right = create(root.right, 2 * i + 2, n, lis)
    return root


def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def mirror(root):
    if root is None:
        return
    else:
        mirror(root.right)
        print(root.data, end=" ")
        mirror(root.left)


if __name__ == "__main__":
    n = int(input())
    lis = list(map(int, input().split()))
    root = node(None)
    root = create(root, 0, n, lis)
    inorder(root)
    print()
    mirror(root)
