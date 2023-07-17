n = int(input("enter size of list"))
lis = list(map(int, input("enter list").strip().split()))
key = int(input("enter key"))


def binary_search(lis, low, high, k):
    while low <= high:
        mid = (low + high) // 2
        if lis[mid] == k:
            return mid
        elif lis[mid] > k:
            high = mid - 1
        elif lis[mid] < k:
            low = mid + 1
    return -1


print(f"index= {binary_search(sorted(lis),0,n-1,key)}")
