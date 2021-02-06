import random
from art import stages, logo
from words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

#  Testing code
#   print(f'Pssst, the solution is {chosen_word}.')

#  Create blanks
display = []
guesses = []
for _ in range(word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f'You have already guessed the letter {guess}')
    else:
        guesses.append(guess)

        #  Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f'You guessed {guess}.  That is not in the word.  You lose a life.')
            lives -= 1
            if lives == 0:
                print('You lose')
                end_of_game = True

        print(f"{' '.join(display)}")

        if '_' not in display:
            print('You win!!!')
            end_of_game = True

        print(stages[lives])
