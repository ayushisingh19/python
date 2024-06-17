class Student:
    quali = "M.Tech"   # static variable declare inside the class   
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.school = "SHSS"  # static variable declare inside the constructor
    def display(self):
        Student.gread = "P.hd"   # static variable declare inside the instence variable
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Quali =",Student.quali)  # static variable access inside the class through class name
        print("School = ",Student.school) # static variable access inside the class through class name
        print("Gread = ",Student.gread) # static variable access inside the class through class name
        print("Achivment = ",Student.achivment)   # static variable access inside the class through class name

obj = Student("Neeraj",37)
Student.achivment="Gate-qualified"   # static variable declare outside of the class
print("Access through class_Name = ",Student.quali) # static variable access outside the class through class name
print("Access through object = ",obj.quali) # static variable access outside the class through object
obj.display()
print("Access through class_Name = ",Student.gread) # static variable access outside the class through class name
print("Access through class_Name = ",Student.school)# static variable access outside the class through class name
print("Access through class_Name = ",Student.achivment)# static variable access outside the class through class name
# obj.display()