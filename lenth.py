# lis=["apple","banana","orange"]
# for i in lis:
#     print(i,"---->",len(i))


# lis=["raj","anup","oom","aman","anup"]
# a=lis.index("anup")
# b=lis.index("anup",a+1)
# print(b)


lis=["anup","raj","vaibhav","aniket","anup","priya","kishan","anup"]
num=int(input("delete the number which you want"))
b=0
for i in range(num):
    a=lis.index("aniket",b)
    b=a+1
lis.pop(a)
print(lis)