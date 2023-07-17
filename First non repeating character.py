"""
input:
acababab
output:
c
input:
aababab #no repeating character
output:
-1.
"""
s = input()
lis = list(s)
freq = {}
c = -1
for i in lis:
    if i in freq:
        freq[i] += 1  # getting frequency
    else:
        freq[i] = 1
# values stored in dictionary
for key in freq:
    if freq[key] == 1:  # getting first non_repeating character
        c = key
        break
print(c)
