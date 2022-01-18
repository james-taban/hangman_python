
#import files and modules
import random
from hangman_art import logo , stages
from hangman_words import word_list

#declare variables
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 7
minus = -1

#printing the logo
print(logo)
#Testing code, you can comment this out
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

      #If the user has entered a letter they've already guessed, print the letter and let them know.

    if guess in display:
      print(f"You have already entered the letter {guess}")
    

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print("The letter you have guessed is not in the word, you lose a life.")
        lives -= 1
        print(f"You have {lives} lives remaining")
        print(stages[minus])
        minus -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
          

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    