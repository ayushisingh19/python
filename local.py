class student:
  def display(self):
    global a
    a=10
    print("variable of a",a)
  def show(self):
    print("value of a=",a)
  def new():
      print("value of a",a)
obj=student()
obj.display()
# obj.show()
# print("value of a=",a)
student.new()