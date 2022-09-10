import random
def main(): 
    print("Main Menu")
if __name__ == '__main__':
    main()
#------------------------------------------------------------------------------
while True:
    print("Welcome to the Main Menu.\n" "\nList of programs:\n" "[1] To run password generator; [2] To run bmi calculator; [3] to run rock paper scissors; [4] To run pizza delivery; [5] To run tip calculator; [6] To run band name generator; [7] To run leap year checker; [8] To run treasure RPG; [9] To run treasure map.\n")
    selection = input("Select which program you want to run:\n")
#------------------------------------------------------------------------------
    if selection == "1":
#------------------------------------------------------------------------------
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    #------------------------------------------------------------------------------
        print("Welcome to the PyPassword Generator!")
        nr_letters= int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))

        password_list = []
        #will choose random letters based in number got in input
        for char in range(1, nr_letters + 1):
            password_list.append(random.choice(letters))
        for char in range(1, nr_symbols + 1):
            password_list.append(random.choice(symbols))
        for char in range(1, nr_numbers + 1):
            password_list.append(random.choice(numbers))

        #will shuffle the password list
        random.shuffle(password_list)
        #creates a new password based on the password list
        password = ""
        for char in password_list:
            password += char
        print(f"Your password is: {password}")
#------------------------------------------------------------------------------
    elif selection == "2":  
#------------------------------------------------------------------------------
        height = float(input("enter ur height: "))
        weight = float(input("enter ur weight: "))

        bmi = (weight / height ** 2) 

        print(f"your bmi is {bmi} ")

        if bmi > 35:
            print("You are clinically obese! ")
        elif bmi > 30 < 35:
            print("You are obese! ")
        elif bmi > 25 < 30:
            print("You are overweight. ")
        elif bmi > 18.5 < 25:
            print("You have a normal weight. ")
        else: 
            print("You are underweight. ")  
#------------------------------------------------------------------------------            
    elif selection == "3":
#------------------------------------------------------------------------------
        player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        computer_choice = random.randint(0, 2)
        print(f"The Computer chose {computer_choice}\n")
    # if input is rock, paper should win but scissors should lose 
        if player_choice >= 3 or player_choice < 0:
            print("You typed a wrong option, smh.")
        elif player_choice == 0 and computer_choice == 2:
            print("You Win!")
        elif computer_choice > player_choice:
            print("You lose!")
        elif computer_choice == player_choice:
            print("It's a draw!")
        elif computer_choice == 0 and player_choice == 2:
            print("You lose!")
        elif player_choice > computer_choice:
            print("You win!")
        else:   
            print("this should never appear. ")
#------------------------------------------------------------------------------
    elif selection == "4":
#------------------------------------------------------------------------------
        print("Welcome to Goofy ahh's pizza delivery! ")
        size = input("What size do you want? Options: S, M or L. ")
        add_pepperoni = input("Do you want pepperoni? Y or N ")
        extra_cheese = input("Do you want extra cheese? Y or N ")
        bill = 0
#-----------------------------------
        size_s = size == "S"
        size_m = size == "M"
        size_l = size == "L"
#-----------------------------------
        if size_s:
            bill += 15
        elif size_m:
            bill += 20
        elif size_l:
            bill += 25
        else:
            print("Thats the wrong option bro. Try again. ")
#-----------------------------------
        if add_pepperoni == "Y":
            if size_s: 
                bill += 2
            else: 
                bill += 3

        if extra_cheese == "Y":
            if size_s: 
                bill += 1
            else: 
                bill += 2

        print(f"Your pizza will be ${bill} Dollars.")
#------------------------------------------------------------------------------
    elif selection == "5":
#------------------------------------------------------------------------------ 
        print("Welcome to the tip calculator! ")

        total_bill = float(input("What was the total bill? $"))

        tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

        num_ppl = int(input("How many people to split the bill? "))

        divide_value = (total_bill * (1+ tip_percent/100))/num_ppl

        print(f"Each person should pay: ${round(divide_value, 2)}")
#------------------------------------------------------------------------------ 
    elif selection == "6":
#------------------------------------------------------------------------------ 
        print("Welcome to the Band Name Generator.\n")
        city = input("What's the name of the city you grew up in?\n")
        pet = input("What is the name of your pet?\n")
        print("Your band name is " + city,pet + ".")
#------------------------------------------------------------------------------ 
    elif selection == "7":
#-----------------------------------------------------------------------------
        year = int(input("Which year do you want to check? "))
        if year % 4 == 0:
            if year % 100 ==0 :
                if year % 400 == 0:
                    print("Leap year.")
                else:
                    print("Not leap year.")
            else:
                print("Leap year.")
        else: 
            print("Not leap year. ")
#------------------------------------------------------------------------------ 
    elif selection == "8":
#-----------------------------------------------------------------------------
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
#------------------------------------------------------------------------------ 
    elif selection == "9":
#-----------------------------------------------------------------------------
        row1 = ["⬜️","⬜️","⬜️"]
        row2 = ["⬜️","⬜️","⬜️"]
        row3 = ["⬜️","⬜️","⬜"]

        map = [row1,row2,row3]
        print(f"{row1}\n{row2}\n{row3}")
        position = input("Where do you want to put the treasure? ")

        horizontal = int(position[0]) #2
        vertical = int(position[1]) #3

        selected_row = map[vertical - 1]
        selected_row[horizontal - 1] = "X"


        print(f"{row1}\n{row2}\n{row3}")
#------------------------------------------------------------------------------ 
    else:
        print("Wrong option. Try again. \n")
#-----------------------------------------------------------------------------
    run_again = input("\nDo you want to run the program again? Type 'yes' or 'no'\n").lower()

    if run_again not in ('yes', 'y'):
        break
#------------------------------------------------------------------------------ #wrote by hoao, based on udemy's python bootcamp.

