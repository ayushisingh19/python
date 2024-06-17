# my_list=[10,20,30,40,50]
# new_list=[]
# for i in my_list:
#     x=i**2
#     new_list.append(x)
#     print(new_list)


# my_list=[10,20,30,40,50]
# def add(n):
#     return n+5
# x=map(add,my_list)
# print(x)
# print(list(x))

# my_list=[10,20,30,40,50]
# def add(n):
#     return n**2
# x=map(add,my_list)
# print(x)
# print(list(x))


#                                                               ascii
# n=input("enter any name:")
# if len (n)!=1: 
#     print("ascii")
# else:
#     aci=ord(n)
#     print("asciivalue of your input",aci)




# x=input("enter the number")
# def add(n):
#         x=ord(n)
#         y=x+5
#         return chr(y)
# y=map(add,x)
# print(y)



# my_list=[10,15,20,25,30,35]
# def greater(n):
#     if n>=20:
#         return True
# x=filter(greater,my_list)
# print(my_list)



my_list=[10,15,20,25,30,35]
def greater(n):
    if n%2:
        return odd
    else:
        return even
x=filter(greater,my_list)
print(my_list)