# x=3
# print(type(x))
# x=3.5
# print(type(x))

# x=3+3j
# print(type(x))


# x='ayushi'
# y="ayushi"
# z='''my
# name
# is
# ayushi'''
# print(type(x))
# print(type(y))
# print(type(z))



s={10,20,30,40}
print(s)
print(type(s))

s={10,20,30,40,50,60 }
print(s)
print(type(s))


s=set()
print(s)
print(type(s))


s={10,20,30,40,50}
s.add(40)
print(s)



s={10,20,30}
i=[40,50,60,10]
s.update(i,range(5))
print(s)

s={40,50,60,32}
print(s)
print(s.pop())
print(s)


s={40,50,60}
s1=s.copy()
print(s1)


s={10,20,30,40}
s.discard(40)
print(s)

s={10,20,30,40}
print(s)
s.clear()
print(s)


x={10,20,30,40,50}
y={30,40,50,60,70}
print(x.union(y))


x={10,20,30,40,50}
y={30,40,50,60,70}
print(x.intersection(y))
print(x&y)
print(y.intersection(x))
print(y&x)





