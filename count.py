lis=[2,3,4,4,3,55,33,78,3,4,90]

c=lis.count(4)
b=0
for i in range(c):
    a=lis.index(4,b)
    b=a+1
    print(a)


# count use for counting of giving same number 
    
lis=[2,3,4,4,4,2,4,3,5,43]
n=4
a=lis.index(n)
print(a)
b=lis.index(n,a+1)
print(b)
for i in range(len(lis)):
    print(lis[i])