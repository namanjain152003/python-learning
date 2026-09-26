marks=[10,20,30,40,50,30.99]  # mutable sequence of values
print(marks[2])
print(len(marks))

# we can change the values of the list
marks[2]=100
print(marks)

# slicing in the lists is same as the strings
print(marks[2:5])
print(marks[-5:-3])

# list methods

# 1. l.append(val) -> this will help to add new values in the end of the list
marks.append(25)
print(marks)

#2. l.insert(idx,val) -> this will help to add value at specific index
marks.insert(2,35)
print(marks)

#3. l.sort() -> this will arrange in ascending order
marks.sort()
print(marks)

# for descending order
marks.sort(reverse=True)
print(marks)

#4. l.reverse
marks.reverse()
print(marks)