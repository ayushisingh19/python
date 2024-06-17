# if else statement 
# wap to detemine wheather a person is eligible to csat vote or not 1 age/ 2 nationality 
# upper() alphabete (lower to upper) if any
# lower() alphabete (upper to lower) if any
# age=int(input("enter your age"))
# national=input("enter your nationality 'indian' or 'other'")
# national=national.strip() #strip use for space erasing

# if age>=18 and national.lower()=="indian":
#     print("yes u r eligible")
#     print("please vote right person")
#     print("done")
# else:
#     print("not eligible")




age=input("enter your age")
print(type(age))

age=int(input("enter the age"))
if age>=60:
    print("u are eligible go to counter no1")
elif age>=30:
   print("go to counter no2")

elif age>=18:
   print("go to counter no3")
   
else:
    print("not eligibe")
    
    