
# if - else example
# voting system 
age=21
if age==21:
    print("you are eligible for vote")
else:
    print("you are not eligible")
    
# elif example
# traffic light system
color="green"
if color=="green":
    print("go")
elif color=="yellow":
    print("look")
else:
    print("stop") 
    
    
#match case

color=input("Enter the color: ")

match color:
    case "Green":
        print("go")
    case "Yellow":
        print("look")
    case "Red":
        print("stop")
    case _:
        print("Wrong color!")   
    
    
    
    
    