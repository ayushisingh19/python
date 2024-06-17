# class student:
#     def display(self,name):
#         self.name=name
#         print("name=",name)
#     def show(self,age):
#         self.age=age
#         self.display("rahul")
#         print("age=",age)
# obj=student()
# obj.display('ayushi')
# obj.show(37)
# # student.display("raj")


# method 
# class method:

class book:
    price=1000
    def book_detail(self,name,author):
        self.name=name
        self.author=author
    @classmethod
    def update_price(cls,price):
         cls.price=price
    def show_detail(self):
        print('book_name',self.name)
        print('book_author',self.author)
        print('book_price',self.price)
obj=book()
obj.book_detail('python','neeraj')
obj.update_price(2000)
obj.show_detail()