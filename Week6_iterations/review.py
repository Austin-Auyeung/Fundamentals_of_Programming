# ## Break
# for i in range(11):
#     if i > 5:
#         break # just breaks the execution of the loop
#     else:
#         print(i) # 0 to 5
#
#
# ## Continue
# for i in range(11):
#     if i % 2 == 0:
#         continue # skips the current iteration and moves onto the next iteration
#     else:
#         print(i)


'''
Write a program to calculate the sum and average of digits present in a given string
Ex: random289$18str849ing6
Expected Output: Sum - 55, Average - 6.11
'''
# total = 0
# count = 0
# list1 = []
# input_str = input("Enter a string with numbers, letters, and symbols: ")
#
# for char in input_str:
#     if char.isdigit():
#         total += int(char)
#         count += 1
#
# avg = total/count
# print(f"Sum: {round(total, 2)}, Average: {round(avg, 2)}")



'''
Write a program to print the number of digits, letters, and special characters in a given string.
Ex: random289$18str849ing6
Output: Digits: 9, Letters: 12, Symbols: 2
'''
givenStr = "random289$18@str849ing6"
digits = 0
letters = 0
symbols = 0

for char in givenStr:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1

print(f"Digits: {digits}, Letters: {letters}, Symbols: {symbols}")


'''
Number Guessing Game
Choose a target value
Ask the user to guess the value
Display whether the number is greater than or less than the target value and ask the user to guess again
    Ex: Too high! Try again
        Too low! Try again
Keep track of number of guesses
If guesses are > 10 the user loses
Ask the user whether he/she wants to continue the game
Repeat above if yes
'''
# target = 11
# again = "YES"
# numGuesses = 0
#
# while again == "YES":
#     guess = int(input("Guess a number: "))
#     if numGuesses < 11:
#         if guess < target:
#             print("Too low! Try again")
#             numGuesses += 1
#         elif guess > target:
#             print("Too high! Try again")
#             numGuesses += 1
#         else:
#             print("You Win")
#             again = input("Would you like to play again? (Yes or No): ").upper()
#     else:
#         print(f"You guessed {numGuesses} times. You lose!")
#         again = input("Would you like to play again? (Yes or No): ").upper()
# print("Thank You for playing!")


'''
Pattern Practice
'''
rows = int(input("Enter the number of rows: "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print(j * 2, end = " ")
    print()

# i   j
# 0   0, 1
#             0 * 2
# 1   0, 2
#             0 * 2
#             1 * 2
# 2   0, 3
#             0 * 2
#             1 * 2
#             2 * 2

rows = 5

for i in range(rows, 0,  -1):
    for j in range(0, i):
        print(i, end = " ")
    print()

rows = 5

for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()