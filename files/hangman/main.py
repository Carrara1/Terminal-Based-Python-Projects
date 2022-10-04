
from operator import truediv
import random 
from files.hangman.art import stages, logo
from files.hangman.word_list import word_list

#------------------------------------------------------------------------------------------------
print(logo)
print("\n")
#------------------------------------------------------------------------------------------------
chosen_word = random.choice(word_list)
display = []
lives = 6

for letter in range(len(chosen_word)):
    display += "_"
print(display)

endresult = False
#------------------------------------------------------------------------------------------------

while not endresult:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed {guess}")   
         
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess}, that is not in the word!")
        lives -= 1
    if guess == "break":
        break
#------------------------------------------------------------------------------------------------

    if lives == 6: 
        print (stages[6]) 
    if lives == 5: 
        print (stages[5]) 
    if lives == 4: 
        print (stages[4]) 
    if lives == 3: 
        print (stages[3]) 
    if lives == 2: 
        print (stages[2]) 
    if lives == 1: 
        print (stages[1]) 
    if lives == 0: 
        print (stages[0])
        print("You lose! ")
        endresult = True
        break

#------------------------------------------------------------------------------------------------

    print(f"{' '.join(display)}")
                  
    if "_" not in display:
        print(f"The word was: {chosen_word}! You won! \n")
    break

#------------------------------------------------------------------------------------------------