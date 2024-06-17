from functools import reduce

# my_list=[10,30,35,15,40,50,80]
# def max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=reduce(max,my_list)
# print(x)


# my_list=[10,30,35,15,40,50,80]
# def min(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=reduce(min,my_list)
# print(x)

  

my_list=[2,4,5,6,7,8,9,0]
def max(x,y):
    if x>y:
        return x
    else:
        return y
x=reduce(max,my_list)
print(x)




 