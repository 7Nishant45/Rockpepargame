import random

def game() :
 choice = ['stone', 'paper', 'scissors']

 print("Enter your choice",choice)
 print("You want to exit just enter exit :-")


 while True :
    user=input("Enter:-").lower()
    print(f"your choice :{user}")
    
    if user == 'exit' :
        print("Thank You")
        break

    if user not in choice :
        print("Invalid choice plz enter valid")
        continue

    computer=random.choice(choice)
    print(f"computer choice:{computer}")

    if user == computer :
     print("Match tie try next")

    elif(computer == 'stone' and user == 'scissors') or \
          (computer == 'paper' and user == 'stone')  or \
              (computer == 'scissors' and user == 'paper') :
            print("Computer Win Game ...!")
            
    else :
        print("you Win Game..!")
   

game()
