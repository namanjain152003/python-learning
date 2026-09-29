# sets are the collection of unique elements
# sets are mutable but we can not change the individual elements inside a set and these are unordered.

items={1,2,2,2,3}
print(len(items))

# to create the empty set 
empty_set=set()
# to create empty dictionary
empty_dict={}

# SET METHODS

# to add new elements in the set we use add method
items.add(4)
print(items)

# to remove elements we use remove method
items.remove(3)
print(items)

# to clear the whole set we use the clear method
items.clear()
print(items)

# to pop out any random value we can use the pop method
s={1,2,3,4}
s.pop()
print(s)

# to union 2 sets we use s1.union(s2)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.union(s2))

# to intersect to sets we use s1.intersection(s2)
print(s1.intersection(s2))