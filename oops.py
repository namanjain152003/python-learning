# oops is a programming style in which we use obejct and classes which help in making our code more reusable
# class is the blueprint of the object
# object is the isinstance of the class

class Car:
    brand = "Toyota"
    
car1=Car()
car2=Car()
print(car2.brand)
print(car1.brand)

# We use the “.” (Dot Operator) to access properties & methods of objects.

# Attributes are variables and Methods are functions defined inside a class.

# a  constructor is a special method used to initialize newly created objects.
#We use __init__(self,....) the method to define our constructor. Whenever we
# create an object of a class, Python automatically calls the __init__ method.

class Student:
    def __init__(self):
        print("constructor is called...")
    
stu1=Student()

# self is a special parameter which refers to the instance of the class that is calling
# the method. We don’t need to pass it explicitly

class Animal:
    def __init__(self,sound):
        self.sound=sound
    
animal1=Animal("bark")
animal2=Animal("meow")
print(animal1.sound)
print(animal2.sound)
print(animal2.sound,animal1.sound)