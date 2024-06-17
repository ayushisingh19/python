#100-9001
#paradrome number means same from front and back 545,1551,22,44,66
#%IS FROM LAST NO AND // FOR FIRST and use 10


for i in range (100,9001):
    num=i
    sum=0
    while num>0:
        last=num%10
        sum=sum*10+last
        num=num//10
        if i==sum:
            print(i)

