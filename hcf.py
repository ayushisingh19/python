a=int(input("enter the first number"))
b=int(input("enter the second number"))
if a<b:
    small=a
else:
    small=b
flag=0
for i in range(small,1,-1):
    if a%i==0 and b%i==0:
        print("hcf",i)
        flag=1
        break
if flag==0:
    print("no hcf possible")
    
