word1="i love"
word2="python"

print(len(word1))  # this is used to find the length of the strings
print(len(word2))

sentence=word1+" "+word2  # this is the concatenation of the two strings
print(sentence)
print(word1+" "+word2)

print(word1[2])   # this is the indexing in the strings
print(word2[1])


# slicing in the strings
word3="naman"
print(word3[2:4])       #[start index : end index] here end index value is  not included

# the default value case
# for start value we can give zero or blank
# for end value we can give blank or len(word)

print(word3[:])  # this will print the whole string
print(word3[2:]) # this will print  from index 2 to last of the string


# we can slice the string using the negative values as well
# n -> -5  a -> -4  m-> -3  a-> -2  n -> -1

print(word3[-4:-2])  # here also -2 is not included 


# String Formatting:

# format() -> it is the old method
a=10
b=5
sum=a+b
print("sum is {}".format(sum)) 
print("sum of {} and {} is {}".format(a,b,sum))

# by index based
print("sum of {0} and {1} is {2}".format(a,b,sum))  # here a is at 0 , b at 1 and sum at 2

# value based
print("sum of {a} and {b}".format(a=10,b=5))
print("sum of {a} and {b} is {sum}".format(a=a,b=b,sum=a+b))


# f strings are the new method 
print(f"sum of {a} and {b} is {sum}")