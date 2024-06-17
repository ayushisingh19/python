# nasting
# complex statement inside the body of complex
name=input("enter your name")
adress=input("enter ypur address")
cat=input("enter 'L' for laptop 'pc' for desktop:")
amount=float(input("enter your cost price"))
if cat=='L':
    if amount<25000:
        dis=0
    elif amount>=25001 and amount<=50000:
       dis=amount*0.5
elif cat=='pc':
    if amount<25000:
        dis=0
    elif amount>=25001 and amount<=50000:
       dis=amount*0.5
else:
    print("invalid catogry")
print(cat,"bill")
print(name,"your name")

