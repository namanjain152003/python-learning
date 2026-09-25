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