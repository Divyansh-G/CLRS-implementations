s = input().strip().split()    # ask user for input, make a list of the numbers provided
s = [int(a) for a in s]        # convert the values in the list from str to int

## insertion-sort: Non-decreasing Order
for j in range(1,len(s)):
    key = s[j]
    i = j-1
    while i >= 0 and s[i] > key:
        s[i+1] = s[i]
        i = i - 1
    s[i+1] = key 

print(s)
