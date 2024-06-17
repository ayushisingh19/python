limit=int(input("enter the range"))
num=int(input("enter the number"))
lowest=num
while limit<1:
    num=int(input("enter the number"))
    if num<lowest:
        lowest=num
        limit-=1
print("lowest:",lowest)
