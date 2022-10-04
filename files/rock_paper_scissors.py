import random
#------------------------------------------------------------------------------

while True:
# start game loop
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = random.randint(0, 2)
    print(f"The Computer chose {computer_choice}")
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

    play_again = input("Do you want to play again? Type 'yes' or 'no'\n").lower()

    if play_again not in ('yes', 'y'):
        break   
  


