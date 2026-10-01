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

# types of Constructors
# 1. Default Constructors - A constructor with no parameters except .
# 2. Parameterized Constructors - Takes parameters to initialize values uniquely for each object.

# Note - Python doesn’t support constructor overloading directly (like Java/C++) i.e. having multiple constructors in the same class. 
# Whichever is written last is executed.

class City:
    def __init__(self):
        print("constructor called...")
        
    def __init__(self,name):
        self.name=name
        
city1=City("delhi")
print(city1.name) # here default constructor will be replaced by parameterised constructor 

# Types of Attributes

# 1. Class Attributes
# • Belong to the class itself, shared by all objects.
# • Defined outside any method in the class.
class Student:
    college = "ABC college" # class attribute
stu1 = Student ()
print(stu1.college)
print(Student.college) # class attribute can also be accessed with class name


# Instance Attributes
# • Belong individually to each object
class Student:
    def __init__ (self, name, gpa): # instance attributes
        self.name = name
        self.gpa = gpa
stu1 = Student("Rahul", 8.7)
print(stu1. name, stu1.gpa)


# types of methods

# 1. instance method
# first parameter is self
# access the class and instance attributes

# 2. class method
# first parameter is cls
# access the class attributes
# decorator -> @classmethod

# 3. static method
# no compulsory parameter
# dont access the class and instance attributes
# decorator -> @staticmethod