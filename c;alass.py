totalclass=int(input("enter the no of class"))
atandclass=int(input("enter the no of attand cclass"))
ap=(atandclass/totalclass)*100
if ap>=75:
    print("you are eligible for exam")
elif ap<=75:
    print("you are not eligible for exam")

