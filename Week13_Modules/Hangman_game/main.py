import random
from hangman_ascii import stages, logo
from words import words

# words = ["forest", "mountain", "ocean", "surprise"]
# chosen_word = random.choice(words).lower()
chosen_word = random.choice(words)  # Uses the imported file to choose a random word from the list inside the file
len_chosen_word = len(chosen_word)  # gets the length of the random word
print(chosen_word)
word_display = []  # empty list to display the length of the word
for _ in range(len_chosen_word):  # appends the list with a placeholder to display the length of the word, 0 to length of the word place an "_" in each index of the list
    word_display.append("_")
print(word_display)
game_over = False  # declare false until it is changed to true when the player wins
incorrect_guesses = []  # empty list to store the already guessed letter to prevent duplicates
lives_left = 7  # set number of lives for the player

print(logo)
while not game_over:  # while game_over variable is not true continue running the while loop
    guess_letter = input("Guess a letter: ").lower()  # asks the player for a guess
    if guess_letter in word_display or guess_letter in incorrect_guesses:  # checks if the player got the letter correct in the list or if the letter is already in the guessed list (only one will be true)
        print(f"You have already guessed {guess_letter}. Try again")  # will print if enters this if statement. Will be same output for either situation since you have already guessed the letter, right or wrong
        print(f"You have {lives_left} lives left.")  # display lives left
    elif guess_letter not in chosen_word:  # if the users guess is not in the word and does not fall into duplicate letter if statement
        print(f"Your guess '{guess_letter}' is not present in the chosen word. You lose a life.")  # display that the guess is wrong and a life will be lost
        lives_left -= 1  # subtract a life from lives_left variable (declared at the start)
        print(f"You have {lives_left} lives left.")  # display lives left
        incorrect_guesses.append(guess_letter)  # add the incorrect guess into the list of incorrect letters, so it can be checked again in the first if statement for a duplicate

        if lives_left == 0:  # if the players lives is 0
            game_over = True  # the game over variable will be changed to true thus ending the while loop
            print("Game over. You lose.")  # display game over before and the while loop ends
    else:  # when the guess is correct fall into this else
        for idx, val in enumerate(chosen_word):  # for loop to find the position of the guess letter against the random word, idx being index and val being the letter at that index
            if val == guess_letter:  # if the word at the index is the same as the users guess letter
                word_display[idx] = guess_letter  # the current index in the random word is the same as the word display placeholder list, so it will be used to be changed to the users correct guess
    print(word_display)
    if '_' not in word_display:  # if there are no more blank spaces in the list then
        game_over = True  # the game over variable will be changed to true and ending the while loop
        print("Game over. You win.")  # display the game over win message and the while loop ends
    print(stages[lives_left])  # using the file import based on the players lives left to display the hangman picture
    ## used outside the if statements because it should always display after going through the if statements
