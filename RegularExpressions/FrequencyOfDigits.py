"""
input:
1v88886l256338ar0ekk

output:
1 1 1 2 0 1 2 0 5 0
"""
import re

s = re.sub("[^0-9]", "", input())
d = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
lis = list(s)
for i in lis:
    d[int(i)] += 1
print(*d.values())
