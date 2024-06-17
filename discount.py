cp=int(input("enter the cost price"))
if cp>0 and cp<=2000:
    dis=cp*0.05
    print("you got a discount of",dis)
    print("you have to pay",cp-dis)
elif cp>=2001 and cp<=5000:
    dis=cp*0.25
    print("you got a discount of",dis)
    print("you have to pay",cp-dis)
elif cp>=5001 and cp<=10000:
    dis=cp*0.35
    print("you got a discount of",dis)
    print("you have to pay",cp-dis) 
elif cp>10000:
    dis=cp*0.50
    print("you got a discount of",dis)
    print("you have to pay",cp-dis) 
else:
    print("invalid input")