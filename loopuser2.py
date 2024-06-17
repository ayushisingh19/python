postive=0
negtive=0
zero=0
while True:
    num=int(input(" enetr number "))

    if num>0:
        postive+=1
    
    elif num<0:
        negtive+=1
        
    else:
        zero+=1
    ch=input("do you want to continue 'yes' or 'no':")
    if ch==' yes ':
        continue
    elif ch=='no':
        print("thankyou")
        break
print("postive number:",postive)
print("negtive number:",negtive)
print("zero number:",zero)
