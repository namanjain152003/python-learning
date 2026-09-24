# functions has two parts definition and calling part

def hello():
    print("hello world")
    
hello()

# we can give parametes to the function

def sum(a,b):
    s=a+b
    return s

ans=sum(4,5)
print(ans)

#another method

print(sum(4,5))


#default parameter

def add(a,b=1):   # important point -> the non default values always come first and then default value
    p=a+b
    return p

print(add(5))