class node:
    def __init__(self, x):
        self.data = x
        self.left = self.right = None


# creation
def create(root, x):
    if root is None:
        return node(x)
    elif root.data > x:
        root.left = create(root.left, x)
    else:
        root.right = create(root.right, x)
    return root


# rightview
def rightview(root):
    if root is None:
        return
    else:
        lis = []
        lis.append(root)
        while len(lis) != 0:
            n = len(lis)
            while n > 0:
                x = lis[0]
                lis.pop(0)
                if n == 1:
                    print(x.data, end=" ")
                if x.left:
                    lis.append(x.left)
                if x.right:
                    lis.append(x.right)
                n -= 1


if __name__ == "__main__":
    n = int(input())
    lis = list(map(int, input().split()))
    root = None
    for i in lis:
        root = create(root, i)
    rightview(root)
