num=int(input("enter range"))

sum=0
odd=0
for i in range(num+1):
    n=int(input("enter number"))
    if(n%2==0):
        sum=sum+n
    else:
        odd+=n
        print("sum of even number is :-",sum)
        print("sum of odd number is :-",odd)
