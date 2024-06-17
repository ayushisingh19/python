lis=[22,44,6,-9,54,6]
h=lis[0]
for i in lis:
    if i>h:
        h=i
print(lis)
print("highest",h)


lis=[22,44,6,-9,54,6]
l=lis[0]
for i in lis:
    if i<l:
        l=i
print(lis)
print("lowest",l)