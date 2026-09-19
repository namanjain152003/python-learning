name="naman"
age=23
gender="male"

isPrime=None
isBool=True

print(name)
print("my name is :",name)
print(type(gender))


#this is a comment 
''' 
this is multi line comment

'''

#arithmetic operator(+,-,*,/,**,%)
#relational operator(<,<=,>,>=,==,!=)
#assignment operator(=,+=,-=,*=,/=)
#logical operator(not , and , or)


'''
operator precedence
()
**
*,/,%
+,-
==,=<,>=,<,>
not
and 
or

'''

#type conversion
# two types of conversion

# 1.implicit(doing on their own)
# e.g  float+int=float

# 2.explicit(done by developer)
# e.g value=float(10)
#     print(value, type(value))

a=float(input("enter value of a"))
#print(a)
#input always take in string form

b=int(input("enter value of b"))
print(a+b)

#average of 2 numbers
p=float(input("enter 1st number: "))
q=float(input("enter 2nd number: "))
avg=(p+q)/2
print(avg)



