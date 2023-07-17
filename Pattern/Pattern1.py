"""
input:5

output:
5 5 5 5 5 5 5 5 5
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
"""

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # left half triangle
        print(n + 1 - j, end=" ")
    for j in range((2 * n - 2 * i) + 1):
        # middle full triangle
        print((n + 1 - i), end=" ")
    for j in range(i, 1, -1):
        # right half triangle
        print(n + 2 - j, end=" ")
    print(" ")
for i in range(1, n):
    for j in range(1, n - i + 1):
        # left half triangle
        print(n + 1 - j, end=" ")
    for j in range(2 * i):
        # middle full triangle
        print((i + 1), end=" ")
    for j in range(i + 1, n + 1):
        # right half triangle
        print(j, end=" ")
    print(" ")
