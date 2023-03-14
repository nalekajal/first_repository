a=23
b=34
c=a+b
print(c)
print ('hello')
lis=[i for i in range (1,20) if i%2==0]
print(lis)

lis={i:i for i in range(1,30) if i%2==1}
print(lis)

class carmodel:
    name="bmw"
    gear=6
    def run(self):
        print("car name is",self.name)
        print("car gear is",self.gear)
obj=carmodel
print(obj.name)
print(obj.gear)


class carmodel:
    name="brezza"
    gear=4
    gear1=7
    def fun(self):
        print("car name is ",self.name)
        print("car gear is",self.gear)
    def fun2(self):
        print("car gear1",self.gear1)
obj=carmodel
print(obj.name)
print(obj.gear)
print(obj.gear1)

class fruit:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def value(self):
        print("the fruit name is",self.name)
        print("the price of fruit is ",self.price)
fruit_obj=fruit("apple",300)
print(fruit_obj.name)
print(fruit_obj.price)
fruit_obj .value()

class fruit:
    def __init__(self,name,price,mono):
        self.name=name
        self.price=price
        self.mono=mono
    def fun1(self):
        print("the fruit name is",self.name)
        print("the price of fruit",self.price)
        print("the mono is",self.mono)
    def fun2(self):
        print("the mono is",self.mono)
fruit_obj=fruit("watermelon",400,7666893936)
print(fruit_obj.name)
print(fruit_obj.price)
print(fruit_obj.mono)
fruit_obj.fun1()
fruit_obj.fun2()


class student:
    def __init__(self,name,roll_no,div,marks):
        self.name=name
        self.roll_no=roll_no
        self.div=div
        self.marks=marks
    def fun1(self):
        print("the student name is",self.name)
        print("the roll_no is",self.roll_no)
        print("div is",self.div)
        print("the marks are",self.marks)
obj_student=student("kajal",11,'A',90)
print(obj_student.name)
print(obj_student.roll_no)
print(obj_student.div)
print(obj_student.marks)
obj_student.fun1()
