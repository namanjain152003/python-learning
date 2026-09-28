# dictionary are the key value pairs and it is mutable.

info={
    "name":"naman",
    "age":23,
    "subjects":["maths","science"]
}

print(info)
print(info["name"])

info["age"]=22
print(info["age"])

# dictionary methods

# 1. d.keys() -> it gives all the keys in the dictionary
print(info.keys())
# we can convert this into list as well
print(list(info.keys()))

# 2. d.values() -> it gives all the values
print(info.values())

# 3. d.items() -> it gives all the key values
print(info.items())

# 4. d.get(val) -> it gives the value acc. to the key
print(info.get("age"))

# this method is used because if we use the wrong key then the flow of code will not be stopped and we get the NONE in the outcome 
# but if we use print(info["key"]) method with wrong key it will stop the flow of the code and give the error

# 5. d.update({val}) ->this will help to add new key and value in the dictionary
info.update({
    "city":"Delhi"
 }) 
print(info)
