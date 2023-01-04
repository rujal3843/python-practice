class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def func(self):
    print("method ="+ self.name)
p1 =Person("rujal",21)
p1.func()