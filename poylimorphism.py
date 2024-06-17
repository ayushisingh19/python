# class a:
#     def new(self,a,b):
#         return a+b
# class b:
#     def new(self,x,y,z):
#         return x+y+z
# obj=a()
#print  (obj.new(5,6))
# # obj.new(5,6,7)




'''class a:
    def new(self,x=0,y=0,z=0):
        return x+y+z

obj=a()
print (obj.new(5,6))
print (obj.new(5,6,7))
print(obj.new(5))
print(obj.new())'''

'''class a:
    @dispatch(int,int)
    def add(self,x,y):
        print(x+y)
    @dispatch(int,int,int)
    def add(self,x,y,z):
        print(x+y+z)
obj=a()
obj.add(5,6)
obj.add(5,6,7)   '''      

class A:
    def add(self,a,b):
        print("output from parent class")
class B(A):
    def add(self,x,y):
        print("output from child class") 
        super().add(4,5 )    
obj=B()
obj.add(5,6)
        

