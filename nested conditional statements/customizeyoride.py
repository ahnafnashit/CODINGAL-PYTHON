print("select yo ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("enter yo choiceee: ") )

if(choice == 1): 
    print("what type of bike? ")
    print("1. Scooty\n")
    print("2. Scooter\n")

    choice2=int(input("Enteer your choice2: "))
    if choice2==1: 
        print("you have selected scooty")
    else: 
        print("you have selected scooter")
#user entering option 2
    
    elif( choice == 2): 
print("what type of car? ")
print("1. Sedan")
print("2. SUV")
choice3=int(input("enter your choice3: "))
if choice3==1: 
    print("you have selected sedan")
else:
    print("you have selected SUV")

else: print("Wrong choice !")