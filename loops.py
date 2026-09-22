# While loop

counter=1
while (counter<=5):
    print("hello world")
    counter+=1
    
    
# break and continue

    # break
    i=1
    while(i<=10):
        if(i%6==0):
            break
        print(i)
        i+=1
    print("out of loop")
    
    # continue
    i=1
    while(i<=10):
        if(i%6==0):
            i+=1
            continue
        print(i)
        i+=1
    print("out of loop")
    
    
    # for loops
    
    word="hello"
    for var in word:
        print(var)
        
    for i in range(5):  #this will work for 0 to n-1  and in-> is a membership operator
        print(i)