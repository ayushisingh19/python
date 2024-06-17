# wap to create a list of n element
# also create a seperate list of even and odd numbers

lis=[]
liss=[]
lisss=[]
n=int(input("enter th range:"))

for i in range(n):
    num=int(input("enetr the number:"))
    lis.append(num)
    print(lis)
    if(num%2==0):
        liss.append(num)
    else:
        lisss.append(num)
print(lis)
print("even num",liss)
print("odd num",lisss)
    