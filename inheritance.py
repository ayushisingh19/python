# # mutilevel inhertitance
# class a:
#     name="ayushi"
#     def m1(self):
#         return"this is m1 method"
# class b(a):
#     age=20
#     def m2(self):
#         print("name=",a.name)
#         print("m1=",self.m1())
# class c(b):
#     def m3(self):
#         print("age=",b.age)
#         self.m2()
# obj=c()
# obj.m3()

# multilple inheritance

# class parent1:
#          def m1(self):
#              print("parent1 method call")
# class parent2:
#          def m1(self):
#               print("parnet2 method call")
# class child(parent1,parent2):
#           def m2(self):
#                 self.m1()
# obj=child()
# obj.m2()



class parent1:
         def m1(self):
             print("parent1 method call")
class parent2:
         def m2(self):
              print("parnet2 method call")

class child(parent2,parent1):
          def m3(self):
                self.m1()
                self.m2()
obj=child()
obj.m3()

