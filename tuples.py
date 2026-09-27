tup=(1,2,3,4,2,5,"abc") #these are immutable sequence of values

print(tup)
print(tup[2])
print(len(tup))

# to create a single value tuple we have to
mp=(5.)

# loops are similar as lists

# we can not change values in tuples

# slicing is also similar in this as lists

# tuples mathod

# 1.t.index(val) -> this gives the index of the first occurance of the given value
print(tup.index(2))

# 2.t.count(val) -> gives the count of the total occurance of the given value
print(tup.count(2))