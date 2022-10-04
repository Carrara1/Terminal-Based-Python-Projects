print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")
choice1 = input("You're at a cross road. Where do you want to go? " + 'Type "left or "right" ').lower()
#---
gameover = "Game Over. "
winmsg = "You found the treasure. You win! "
wrongchoice = "Wrong choice bud. "
#---

if choice1 == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ").lower()
            if choice3 == "red":
                print(gameover)
            elif choice3 == "yellow":
                print(winmsg)
            elif choice3 == "blue":
                print(gameover)
            else:
                print(wrongchoice)
    else:
        print(gameover) 
elif choice1 == "right":
    print("You fell into a hole. ")
    print(gameover)
else: 
    choice1 == "left" or "right" == False
    print(wrongchoice)
    print(gameover)