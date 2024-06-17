# wap to determine perxson is eligible for vote or not 
age=int(input("enter your age"))
nation=int(input("you are indian 'yes' or 'no'"))
nation=nation.strip()
if age>=18 and nation.upper()=="YES":
    print("yes you are eligible")
else:
    print("not eligible")


