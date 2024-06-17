# touple concatenate
#  min(),max(),len(),count(),index() functions
# sorted and any are also a functions
# any give bollean output (true and flase)
t=(1,2,3)
t1=(33,66)
t=t+t1
print(t)


s="apple"
s=tuple(s)
print(s)

c=tuple()
print(c)
print(any(c)) 
# database fatch


lis=[2,3,4,5]
lis=tuple(lis)
print(lis)

t=24,2,5,-2,99
lis=sorted(t)
print(lis)

t=2,3,4,7,3
a=max(t)
print(a)

t=2,3,4,5,6
a=min(t)
print(a)


t=3,4,5,6,7
a=len(t)
print(a)


t=4,5,6,7,9
a=t.index(9)
print(a)

t=3,4,5,8,9,3,2,4,5,3,3,2
a=t.count(3)
print(a)


t=2,3,4,5,6,7
b=t.index(2)
print(b)
