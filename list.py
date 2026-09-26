marks=[10,20,30,40,50,"abc",30.99]  # mutable sequence of values
print(marks[2])
print(len(marks))

# we can change the values of the list
marks[2]=100
print(marks)

# slicing in the lists is same as the strings
print(marks[2:5])
print(marks[-5:-3])
