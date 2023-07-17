def isminheap(lis, n, i):
    if i >= int((n - 2) / 2):
        return True

    if (
        lis[i] < lis[2 * i + 1]
        and lis[i] < lis[2 * i + 1]
        and isminheap(lis, n, 2 * i + 1)
        and isminheap(lis, n, 2 * i + 2)
    ):
        return True

    return False


if __name__ == "__main__":
    n = int(input())
    lis = list(map(int, input().split()))
    print(isminheap(lis, n, 0))
